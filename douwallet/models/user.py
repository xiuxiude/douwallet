from douwallet.models import db
import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password_digest = db.Column(db.String(128))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Description for superadmin
    def __unicode__(self):
        return self.username

    # Authentication
    @property
    def password(self):
        return self.password_digest

    @password.setter
    def password(self, value):
        self.password_digest = bcrypt.hashpw(value, bcrypt.gensalt())

    def authenticate(self, password):
        return bcrypt.hashpw(password, self.password_digest) == self.password_digest

    # Get user by login(username or email)
    @classmethod
    def get_by_login(cls, login):
        user = cls.query.filter_by(username=login).first()
        if not user:
            user = cls.query.filter_by(email=login).first()
        return user

    # Get user by id
    @classmethod
    def get(cls, id_):
        return cls.query.filter_by(id=id_).first()
