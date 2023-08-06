import sys
import re

from tornado.web import authenticated

from jupyterhub.handlers.base import BaseHandler

from ..version import __version__


class AdminHandler(BaseHandler):
    @authenticated
    async def get(self):
#        current_user = await self.get_current_user()
        html = self.render_template(
            "jupyter-admin.html",
            base_url=self.settings['base_url']
        )
        template_html = await html
        self.write(template_html)
