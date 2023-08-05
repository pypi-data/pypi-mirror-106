from typing import List

from fastapi import BackgroundTasks
from kyosk.config import config
from kyosk.exception import InvalidWorkspaceException, TaskNotFoundException
from kyosk.service.colaborativo import ColaborativoService
from kyosk.user_case.kyosk_user_case import kyosk_user_case
from kyosk.user_case.task_user_case import task_user_case

from .schema import TaskIn, TaskOut

_colaborativo_service = ColaborativoService()


class TaskController:
    async def create(self, new_task: TaskIn, background_tasks: BackgroundTasks) -> str:
        if new_task.metadado.workspace not in str(config.api.workspace_allow):
            raise InvalidWorkspaceException()

        sftp_credentials = await _colaborativo_service.get_sftp_credentials(
            new_task.campaign_id
        )

        task_id = await kyosk_user_case.start_upload(
            new_task, sftp_credentials, background_tasks
        )
        return task_id

    def get_all(self) -> List[TaskOut]:
        all = task_user_case.find_task(hide_rename_status=True)
        return all

    def get_by_id(self, task_id: str) -> TaskOut:
        task = task_user_case.find_task(task_id=task_id, hide_rename_status=True)
        if not task:
            raise TaskNotFoundException(f"Task {task_id} doesn't  exists.")
        return task
