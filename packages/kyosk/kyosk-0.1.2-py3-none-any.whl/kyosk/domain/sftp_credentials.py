from pydantic import BaseModel


class SftpCredentials(BaseModel):
    host: str
    user: str
    password: str
    port: int
    remote_base_path: str

    @staticmethod
    def from_data(
        *, host: str, user: str, password: str, port: int, remote_base_path: str
    ) -> "SftpCredentials":
        return SftpCredentials(
            host=host,
            user=user,
            password=password,
            port=port,
            remote_base_path=remote_base_path,
        )

    def simple_info(self,):
        return dict(host=self.host, path=self.remote_base_path)
