from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends
from kyosk.api.controller.task.schema import TaskIn, TaskOut
from kyosk.api.controller.task.task_controller import TaskController

router = APIRouter()


@router.post("/")
async def create_task_to_upload_using_sftp(
    new_task: TaskIn,
    background_tasks: BackgroundTasks,
    task_controller: TaskController = Depends(),
):

    return await task_controller.create(
        new_task=new_task, background_tasks=background_tasks
    )


@router.get("/", response_model=List[TaskOut])
def get_all_tasks(task_controller: TaskController = Depends(),):
    return task_controller.get_all()


@router.get("/{task_id}", response_model=TaskOut)
def get_one_task(
    task_id: str, task_controller: TaskController = Depends(),
):
    return task_controller.get_by_id(task_id=task_id)
