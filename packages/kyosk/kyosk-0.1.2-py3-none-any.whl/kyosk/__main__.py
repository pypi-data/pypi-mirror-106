import uvicorn
from kyosk.api import create_app
from kyosk.config import config

app = create_app()
if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.api.bind.address,
        port=config.api.bind.port,
        debug=config.api.debug_mode,
    )
