#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, request, redirect, url_for, render_template
from flask.ext import login
from flask.ext.wtf import Form

import wtforms as wtf
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo, Regexp

from douwallet.models.user import User

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/')
def index():
    if login.current_user.is_authenticated():
        return redirect(url_for('home.index'))
    else:
        return redirect(url_for('auth.login'))


# Define login and registration forms
class LoginForm(Form):
    login = wtf.TextField(validators=[Required()])
    password = wtf.PasswordField(validators=[Required()])

    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise ValidationError('Invalid user')

        if not user.authenticate(self.password.data):
            raise ValidationError('Invalid password')

    def get_user(self):
        return User.get_by_login(self.login.data)


class RegistrationForm(Form):
    username = wtf.TextField(validators=[Required(),
                                         Regexp(r'[A-Za-z0-9_\.]+',
                                                message="Invalid username")])
    email = wtf.TextField(validators=[Required(), Email()])
    password = wtf.PasswordField(validators=[Required()])
    confirm = wtf.PasswordField(
                    validators=[
                        Required(),
                        EqualTo('password', message="Passwords must match")])

@bp.route('/login', endpoint="login", methods=['GET', 'POST'])
def login_view():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = form.get_user()
        login.login_user(user)
        next_ = request.args.get('next')
        if next_:
            return redirect(next_)
        return redirect(url_for('home.index'))
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    login.logout_user()
    return redirect(url_for('home.index'))
