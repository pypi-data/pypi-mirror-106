from kyosk.domain.sftp_credentials import SftpCredentials


class AuthenticatorInterface:
    async def get_sftp_credentials(self, campaign_id: int) -> SftpCredentials:
        raise NotImplementedError
