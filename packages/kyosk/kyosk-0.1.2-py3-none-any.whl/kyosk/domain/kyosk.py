from kyosk.domain.interface.sftp_client_interface import SftpClient
from kyosk.domain.media import MediaContainer


class Kyosk:
    def upload_medias_sftp(
        self, sftp_client: SftpClient, remote_path: str, media: MediaContainer
    ):
        sftp_client.send_media(media, remote_path)
