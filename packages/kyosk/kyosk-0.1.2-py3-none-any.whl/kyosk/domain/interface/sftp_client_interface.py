from kyosk.domain.media import MediaContainer
from kyosk.domain.sftp_credentials import SftpCredentials


class SftpClient:
    def __init__(self, credentials: SftpCredentials):
        raise NotImplementedError()

    def send_media(self, media: MediaContainer, remote_path: str):
        raise NotImplementedError()
