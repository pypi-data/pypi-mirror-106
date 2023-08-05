import os
import socket
from queue import Queue
from threading import Thread

from kyosk.domain.media import MediaContainer
from kyosk.domain.sftp_credentials import SftpCredentials
from ssh2.session import Session
from ssh2.sftp import (
    LIBSSH2_FXF_CREAT,
    LIBSSH2_FXF_WRITE,
    LIBSSH2_SFTP_S_IRGRP,
    LIBSSH2_SFTP_S_IROTH,
    LIBSSH2_SFTP_S_IRUSR,
    LIBSSH2_SFTP_S_IWUSR,
)


class DataReader(Thread):
    def __init__(self, file, read_size: int, num_blocks: int, timeout: int):
        super().__init__()
        self.file = file
        self.read_size = read_size
        self.num_blocks = num_blocks
        self.queue = Queue(num_blocks)
        self.timeout = timeout
        self.stop_iter = False

    def run(self):
        data = None
        while not self.stop_iter:
            if not data:
                data = self.file.read(self.read_size)

            if len(data):
                try:
                    self.queue.put(data, timeout=self.timeout)
                    data = None
                except:
                    pass
            else:
                break

    def stop(self):
        self.stop_iter = True

    def get(self):
        return self.queue.get()


class KyoskSftpClient:
    def __init__(self, sftp_credencials: SftpCredentials, timeout: int):
        self._credentials = sftp_credencials
        self._timeout = timeout

    def send_media(
        self,
        file_path: str,
        task_id: str,
        media_container: MediaContainer,
        tmp_remote_media_path: str,
        callback_on_write=None,
        callback_on_finish=None,
    ):
        sftp_config = self._credentials
        mode = (
            LIBSSH2_SFTP_S_IRUSR
            | LIBSSH2_SFTP_S_IWUSR
            | LIBSSH2_SFTP_S_IRGRP
            | LIBSSH2_SFTP_S_IROTH
        )
        file_flags = LIBSSH2_FXF_CREAT | LIBSSH2_FXF_WRITE

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((sftp_config.host, sftp_config.port))
            session = Session()
            session.set_timeout(self._timeout * 1000)
            session.handshake(sock)
            session.userauth_password(sftp_config.user, sftp_config.password)
            sftp_client = session.sftp_init()
            with open(file_path, "rb") as local_fh, sftp_client.open(
                tmp_remote_media_path, file_flags, mode
            ) as remote_fh:
                local_fh.seek(0, os.SEEK_END)
                file_size = local_fh.tell()
                local_fh.seek(0)

                try:
                    data_reader = DataReader(
                        local_fh, 1024 * 1024 * 2, 32, self._timeout
                    )
                    data_reader.start()
                    data_sent = 0
                    while data_sent < file_size:
                        data = data_reader.get()
                        ret_code, bytes_written = remote_fh.write(data)
                        data_reader.queue.task_done()
                        data_sent += bytes_written
                        if callback_on_write:
                            callback_on_write(
                                task_id, media_container, data_sent, file_size
                            )

                    if callback_on_finish:
                        callback_on_finish(
                            task_id, media_container, file_size, file_size,
                        )
                finally:
                    data_reader.stop()
                    data_reader.join()

        except Exception as ex:
            sock.close()
            raise ex
