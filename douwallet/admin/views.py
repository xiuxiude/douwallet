from flask import redirect, url_for

from flask.ext.superadmin import AdminIndexView
from flask.ext import login

class IndexView(AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

    def _handle_view(self, name, *args, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))
