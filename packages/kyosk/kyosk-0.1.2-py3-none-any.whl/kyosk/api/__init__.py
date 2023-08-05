from fastapi import FastAPI
from kyosk.config import config
from starlette.middleware.cors import CORSMiddleware

from .middleware import install_exception_handlers
from .routes import file_picker, health_check, task, workspace, types


def add_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.api.allow_origins,
        allow_origin_regex=config.api.allow_origin_regex
        if config.api.allow_origin_regex
        else None,
        # allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app():
    app = FastAPI(debug=config.api.debug_mode)

    add_cors(app)

    app.include_router(health_check.router, prefix="/healthcheck")
    app.include_router(file_picker.router, prefix="/openfilepicker")
    app.include_router(task.router, prefix="/task")
    app.include_router(workspace.router, prefix="/workspace")
    app.include_router(types.router, prefix="/type")

    install_exception_handlers(app)

    return app
