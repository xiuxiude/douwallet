#!/usr/bin/env python
# encoding: utf-8

from flask.ext.login import LoginManager

from douwallet.models.user import User

login_manager = LoginManager()

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
