import asyncio
import concurrent.futures
import traceback
from pathlib import Path, PurePosixPath

import asyncssh
from kyosk.config import config
from kyosk.domain.media import MediaContainer, MediaStatus
from kyosk.domain.sftp_credentials import SftpCredentials
from kyosk.service.sftp import KyoskSftpClient
from kyosk.user_case.task_user_case import task_user_case

TIMEOUT = config.task.timeout


def file_transfer_progress_handler(
    task_id: str, media_container: MediaContainer, bytes_sent: int, bytes_total: int
):
    progress = 100 * bytes_sent / bytes_total
    state = MediaStatus.rename if progress == 100.0 else MediaStatus.processing
    task_user_case.update_file_transfer(
        task_id=task_id,
        media_container_id=media_container.id,
        bytes_sent=bytes_sent,
        media_transfer_state=state,
        media_transfer_progress=progress,
    )


async def rename_partials(
    sftp_client: asyncssh.SFTPClient,
    remote_base_path: str,
    media_container: MediaContainer,
    task_id: str,
):
    (
        remote_media_path,
        tmp_remote_media_path,
        remote_xml_path,
        tmp_remote_xml_path,
    ) = get_remote_paths(remote_base_path, media_container)

    try:
        await sftp_client.rename(tmp_remote_media_path, remote_media_path)
        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            media_transfer_state=MediaStatus.success,
        )

    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            media_transfer_state=MediaStatus.error,
            xml_transfer_state=MediaStatus.error,
        )

    try:
        await sftp_client.rename(tmp_remote_xml_path, remote_xml_path)
        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            xml_transfer_state=MediaStatus.success,
        )
    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            xml_transfer_state=MediaStatus.error,
        )


async def send_xml(
    sftp_client: asyncssh.SFTPClient,
    remote_base_path: str,
    media_container: MediaContainer,
    task_id: str,
):
    _, _, _, tmp_remote_xml_path = get_remote_paths(remote_base_path, media_container)
    try:

        xml_buffer = media_container.xml.get_xml_str()

        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            xml_transfer_state=MediaStatus.processing,
        )

        async with sftp_client.open(tmp_remote_xml_path, "wb") as f:
            await f.write(xml_buffer)

        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            xml_transfer_state=MediaStatus.processing,
        )

    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            xml_transfer_state=MediaStatus.error,
        )


def send_media(
    sftp_config: SftpCredentials, media_container: MediaContainer, task_id: str
):
    try:
        remote_base_path = sftp_config.remote_base_path
        local_media_path = Path(media_container.media.path)

        _, tmp_remote_media_path, _, _ = get_remote_paths(
            remote_base_path, media_container
        )

        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            media_transfer_state=MediaStatus.processing,
        )

        KyoskSftpClient(sftp_credencials=sftp_config, timeout=TIMEOUT).send_media(
            file_path=local_media_path,
            task_id=task_id,
            media_container=media_container,
            tmp_remote_media_path=tmp_remote_media_path,
            callback_on_write=file_transfer_progress_handler,
            callback_on_finish=file_transfer_progress_handler,
        )

    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        task_user_case.update_file_transfer(
            task_id=task_id,
            media_container_id=media_container.id,
            media_transfer_state=MediaStatus.error,
        )


def get_remote_paths(remote_base_path: str, media_container: MediaContainer):

    local_file_path = Path(media_container.media.path)
    new_filename = f"{local_file_path.stem}_{media_container.xml.retranca}_{media_container.xml.id}"
    remote_media_path = (
        PurePosixPath(remote_base_path) / f"{new_filename}{local_file_path.suffix}"
    )
    tmp_remote_media_path = str(remote_media_path) + ".partial"

    remote_xml_path = str(PurePosixPath(remote_base_path) / new_filename) + ".xml"
    tmp_remote_xml_path = remote_xml_path + ".partial"

    return (
        remote_media_path,
        tmp_remote_media_path,
        remote_xml_path,
        tmp_remote_xml_path,
    )


async def delete_partials(
    sftp_client: asyncssh.SFTPClient,
    remote_base_path: str,
    media_container: MediaContainer,
):
    _, tmp_remote_media_path, _, tmp_remote_xml_path = get_remote_paths(
        remote_base_path, media_container
    )

    try:
        if await sftp_client.exists(tmp_remote_media_path):
            await sftp_client.remove(tmp_remote_media_path)

        if await sftp_client.exists(tmp_remote_xml_path):
            await sftp_client.remove(tmp_remote_xml_path)
    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)


async def transfer_one(
    executor: concurrent.futures.ThreadPoolExecutor,
    sftp_client: asyncssh.SFTPClient,
    sftp_config: SftpCredentials,
    media_container: MediaContainer,
    task_id: str,
):
    remote_base_path = sftp_config.remote_base_path
    loop = asyncio.get_event_loop()

    await loop.run_in_executor(
        executor, send_media, sftp_config, media_container, task_id
    )
    await asyncio.wait_for(
        send_xml(sftp_client, remote_base_path, media_container, task_id),
        timeout=TIMEOUT,
    )
    await asyncio.wait_for(
        rename_partials(sftp_client, remote_base_path, media_container, task_id),
        timeout=TIMEOUT,
    )


async def perform_transfer(
    task_id: str,
    conn: asyncssh.SSHClientConnection,
    sftp_client: asyncssh.SFTPClient,
    sftp_config: SftpCredentials,
):
    try:
        remote_base_path = sftp_config.remote_base_path
        transfer_tasks = []
        with concurrent.futures.ThreadPoolExecutor(4) as executor:
            task = task_user_case.find_task(task_id=task_id)
            for _, media_container in task.media_containers.items():

                transfer_tasks.append(
                    asyncio.ensure_future(
                        transfer_one(
                            executor, sftp_client, sftp_config, media_container, task_id
                        )
                    )
                )
            if transfer_tasks:
                await asyncio.wait(transfer_tasks)

        delete_futures = []
        for _, media_container in task.media_containers.items():

            media_transfer = media_container.media
            xml_transfer = media_container.xml

            if (
                media_transfer.status == MediaStatus.error
                or xml_transfer.status == MediaStatus.error
            ):
                delete_futures.append(
                    delete_partials(sftp_client, remote_base_path, media_container)
                )
        if delete_futures:
            _, pending = await asyncio.wait(delete_futures, timeout=TIMEOUT)
            if pending:
                map(lambda task: task.cancel(), pending)
                raise Exception("delete_futures did not complete before timeout")
    finally:
        sftp_client.exit()
        conn.disconnect(asyncssh.DISC_BY_APPLICATION, "done")


async def start_transfer_group(sftp_config: SftpCredentials, task_id: str):
    try:
        conn = await asyncio.wait_for(
            asyncssh.connect(
                host=sftp_config.host,
                port=sftp_config.port,
                username=sftp_config.user,
                password=sftp_config.password,
                known_hosts=None,
                compression_algs=None,
                encryption_algs=["aes256-ctr"],
                mac_algs=config.task.mac_algs,
            ),
            TIMEOUT,
        )
        try:
            async with conn.start_sftp_client() as sftp_client:
                await perform_transfer(task_id, conn, sftp_client, sftp_config)
        finally:
            conn.close()
    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        task_user_case.update_file_transfer(task_id=task_id, any_errors=True)
    finally:
        task_user_case.update_file_transfer(task_id=task_id, is_finished=True)
