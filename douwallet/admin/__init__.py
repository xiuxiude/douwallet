from flask.ext.superadmin import Admin
from douwallet.admin.views import IndexView

admin = Admin(index_view=IndexView())

# register model views
from douwallet.models import db
from douwallet.models.user import User
admin.register(User, session=db.session)
