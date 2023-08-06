from typing import Union
from os import PathLike

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


def add_dev_spa_static_handler(
        app: FastAPI,
        directory: Union[str, PathLike],
        html_path: Union[str, PathLike],
        path: Union[str, PathLike] = '/static',
        name: str = 'static'
):
    """
    Add to `app` handler that serves static files and `index.html`. Use only for
    development mode!

    :param app: FastAPI application.
    :param directory: Path to static files.
    :param html_path: Path to HTML file.
    :param path: Route that will handle static file
    :param name: Name that can be used internally by FastAPI

    Example:

    .. code-block:: python

      app = FastAPI()

      # add some handlers...

      # finally, add route '/static' and HTML file handler
      if IS_DEV_MODE:
          add_dev_spa_static_handler(
              app,
              'path/to/static',
              'path/to/index.html'
          )
    """

    app.mount(path, StaticFiles(directory=directory), name=name)

    @app.get('/{full_path:path}')
    async def index():
        with open(html_path, 'r') as html_file:
            return HTMLResponse(html_file.read())
