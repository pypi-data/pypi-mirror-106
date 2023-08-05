import traceback

import aiohttp
from kyosk.config import config
from kyosk.domain.sftp_credentials import SftpCredentials
from kyosk.exception import InvalidCredentialException
from kyosk.service.interface.autenticatitor_Interface import AuthenticatorInterface


class ColaborativoService(AuthenticatorInterface):
    def __init__(self):
        super().__init__()

    async def get_sftp_credentials(self, campaign_id: int):
        headers = {"X-API-Key": config.colaborativo.token_api}
        try:
            async with aiohttp.ClientSession(
                headers=headers, raise_for_status=True
            ) as session:
                async with session.get(
                    f"{config.colaborativo.host}/sftp/campaign/{campaign_id}"
                ) as response:
                    credentials = await response.json()
                    return SftpCredentials.from_data(
                        host=credentials["host"],
                        port=credentials["port"],
                        user=credentials["username"],
                        password=credentials["password"],
                        remote_base_path=credentials["path"],
                    )
        except aiohttp.ClientResponseError as ex:
            if ex.status in [404, 401]:
                raise InvalidCredentialException()
            traceback.print_exception(type(ex), ex, ex.__traceback__)
            raise ex
