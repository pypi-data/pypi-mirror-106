from fastapi import BackgroundTasks
from kyosk.config import config
from kyosk.domain.kyosk import Kyosk
from kyosk.domain.sftp_credentials import SftpCredentials
from kyosk.domain.task import NewTask
from kyosk.service.filePicker import FilePicker
from kyosk.task.sftp_task import start_transfer_group
from kyosk.user_case.task_user_case import task_user_case


class KyoskUserCase:
    def __init__(self):
        self.kyosk = Kyosk()
        self.file_picker = FilePicker()

    async def start_upload(
        self,
        new_task: NewTask,
        sftp_credentials: SftpCredentials,
        background_tasks: BackgroundTasks,
    ):
        task_id = await task_user_case.create(new_task)
        background_tasks.add_task(start_transfer_group, sftp_credentials, task_id)
        task_user_case.clean_up_task_olds(config.task.clean_up_task_time_s)

        return task_id


kyosk_user_case = KyoskUserCase()
