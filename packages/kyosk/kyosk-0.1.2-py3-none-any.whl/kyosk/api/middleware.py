from kyosk import exception
from starlette.requests import Request
from starlette.responses import JSONResponse

ex_responses = {
    exception.TaskNotFoundException: dict(
        default_code=404, default_message="Task não encontrada."
    ),
    exception.InvalidCredentialException: dict(
        default_code=401,
        default_message="Credenciais inválidas. Verifiquei seu token de API.",
    ),
    exception.InvalidWorkspaceException: dict(
        default_code=400, default_message="Envie workspaces válidos.",
    ),
}


def install_exception_handlers(app):
    def handler_factory(exception_class):
        ex_params = ex_responses.get(exception_class)
        if ex_params:
            code, message = ex_params["default_code"], ex_params["default_message"]

            async def handler(request: Request, exc):
                return JSONResponse(status_code=code, content={"detail": message})

            return handler
        else:
            raise Exception("Unknown exception")

    for exception_class in ex_responses:
        handler = handler_factory(exception_class)
        app.exception_handler(exception_class)(handler)
