import string
import time
from datetime import datetime
from pathlib import Path
from random import choices
from typing import List, Optional, Union

from kyosk.domain.media import Media, MediaContainer, MediaStatus, XmlData
from kyosk.domain.task import NewTask, Task
from kyosk.exception import MediaDoesntExistException
from kyosk.util import get_mimetype
from tzlocal import get_localzone

transfers_repository = {}
ID_CHARACTERS = string.ascii_letters + string.digits


def generate_id():
    return "".join(choices(ID_CHARACTERS, k=8))


def get_all() -> List[Task]:
    return list(transfers_repository.values())


def get_one(id: str) -> Optional[Task]:
    return transfers_repository.get(id, None)


def rename_status_hider(tasks: List[Task]):
    for task in tasks:
        for media_container in task.media_containers.values():
            if media_container.media.status == MediaStatus.rename:
                media_container.media.status = MediaStatus.processing
    return tasks


class TaskUserCase:
    async def create(self, new_task: NewTask) -> str:

        media_containers = {}

        for file_path in new_task.media_paths:
            id = str(generate_id())

            _file_path = Path(file_path)
            if not _file_path.exists():
                raise MediaDoesntExistException(f"Media '{file_path}' doesn't exists.")

            media = Media(
                path=str(_file_path.absolute()),
                mimetype=get_mimetype(file_path),
                size=_file_path.stat().st_size,
                name=_file_path.stem,
                status=MediaStatus.pending,
            )
            media_containers[id] = MediaContainer(
                id=id,
                media=media,
                xml=XmlData(
                    id=id,
                    filename=media.name,
                    datetime=datetime.now()
                    .astimezone(get_localzone())
                    .strftime("%Y-%m-%dT%H:%M:%S%z"),
                    description=new_task.metadado.description,
                    card=f"{new_task.metadado.type.value} {new_task.metadado.media_identification}",
                    workspace=new_task.metadado.workspace,
                    username=new_task.username,
                    retranca=new_task.metadado.retranca,
                ),
            )
        id = str(generate_id())
        new_transfer = Task(
            id=id,
            media_containers=media_containers,
            total=sum(
                [
                    media_container.media.size
                    for media_container in media_containers.values()
                ]
            ),
        )
        transfers_repository[id] = new_transfer
        return id

    def update_file_transfer(
        self,
        *,
        task_id: str,
        media_container_id: str = None,
        media_transfer_state: MediaStatus = None,
        media_transfer_progress: float = None,
        bytes_sent: float = None,
        xml_transfer_state: MediaStatus = None,
        is_finished: bool = None,
        any_errors: bool = None,
    ) -> Task:
        current_task = transfers_repository[task_id]

        if media_transfer_state:
            current_task.media_containers[
                media_container_id
            ].media.status = media_transfer_state

        if media_transfer_progress:
            current_task.media_containers[
                media_container_id
            ].media.complete_percentage = media_transfer_progress

            if bytes_sent:
                current_task.media_containers[
                    media_container_id
                ].media.sent = bytes_sent
                current_task.loaded = sum(
                    [
                        media_container.media.sent
                        for media_container in current_task.media_containers.values()
                    ]
                )

        if xml_transfer_state:
            current_task.media_containers[
                media_container_id
            ].xml.status = xml_transfer_state

        if is_finished:
            current_task.is_finished = is_finished

        if (
            any_errors
            or media_transfer_state == MediaStatus.error
            or xml_transfer_state == MediaStatus.error
        ):
            current_task.any_error = True
        return current_task

    def clean_up_task_olds(self, clean_task_time_old_s: int):
        for task in get_all():
            if task.is_finished and task.createdAt + clean_task_time_old_s < int(
                time.time()
            ):
                del transfers_repository[task.id]

    def find_task(
        self, task_id: str = "", hide_rename_status: bool = False
    ) -> Union[List[Task], Task]:
        if not task_id:
            all_tasks = get_all()
            if hide_rename_status:
                all_tasks = rename_status_hider(all_tasks)
            return all_tasks
        else:
            task = get_one(task_id)
            if task and hide_rename_status:
                task = rename_status_hider([task])[0]
            return task


task_user_case = TaskUserCase()
