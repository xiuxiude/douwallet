from flask import redirect, url_for

from flask.ext.superadmin import AdminIndexView
from flask.ext import login

class IndexView(AdminIndexView):
    def is_accessible(self):
        user =  login.current_user
        return (hasattr(user,'is_admin') and user.is_admin)

    def _handle_view(self, name, *args, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))
