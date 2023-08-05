import json
from os import getcwd, getenv
from os.path import exists
from pathlib import Path
from typing import List

from kyosk.domain.task import Type, Workspace
from pydantic import BaseModel

CONFIG_ENV_VAR = "KYOSK_API_CONFIG"

DEFAULT_CONFIG_FILE_NAME = (
    getenv(CONFIG_ENV_VAR) if getenv(CONFIG_ENV_VAR) else "config.json"
)


def get_config_file_path():

    config_file = getenv("KYOSK_APP_CONFIG_FILE")
    if config_file:
        return config_file
    else:
        current_folder = getcwd()
        if current_folder:
            config_file_root = str(Path(current_folder) / DEFAULT_CONFIG_FILE_NAME)
            if exists(config_file_root):
                return config_file_root
            config_file_folder = str(
                Path(current_folder) / "config" / DEFAULT_CONFIG_FILE_NAME
            )
            if exists(config_file_folder):
                return config_file_folder
            else:
                return DEFAULT_CONFIG_FILE_NAME
        else:
            return DEFAULT_CONFIG_FILE_NAME


class ConfigFileDoesNotExistException(Exception):
    pass


class ColaborativoConfig(BaseModel):
    host: str
    token_api: str


class TaskConfig(BaseModel):
    timeout: int
    clean_up_task_time_s: int
    mac_algs: List[str]


class ApiBindConfig(BaseModel):
    address: str
    port: int


class ApiConfig(BaseModel):
    allow_origins: List[str]
    allow_origin_regex: str
    debug_mode: bool
    workspace_allow: List[Workspace]
    types_allow: List[Type]
    bind: ApiBindConfig


class ApplicationConfig(BaseModel):
    colaborativo: ColaborativoConfig
    task: TaskConfig
    api: ApiConfig

    class Config:
        orm_mode = True


json_config = None
path_2_config_file = get_config_file_path()
with open(path_2_config_file) as json_file:
    json_config = json.load(json_file)

try:
    exists(path_2_config_file)
except Exception as ex:
    raise ConfigFileDoesNotExistException(ex)

config: ApplicationConfig = ApplicationConfig(**json_config)
