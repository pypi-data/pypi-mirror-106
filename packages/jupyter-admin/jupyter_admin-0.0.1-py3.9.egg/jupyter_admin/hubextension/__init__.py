import os

from tornado.web import StaticFileHandler

# from jupyterhub.handlers.static import CacheControlStaticFilesHandler

from .main import AdminHandler
from .._data import DATA_FILES_PATH


jupyter_admin_extra_handlers = [
    (r'jupyter-admin', AdminHandler),
    (r'jupyter-admin-static/(.*)', StaticFileHandler, dict(path=os.path.join(DATA_FILES_PATH, "static"))),
]
