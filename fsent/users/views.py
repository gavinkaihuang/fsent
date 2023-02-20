from flask import flash, redirect, render_template, request, url_for, Blueprint, session
from .forms import LoginForm
from fsent import app, db
from fsent.models import User
from flask_login import LoginManager, login_user, logout_user, login_required
from fsent.jsonencoder import UserJSONEncoder
import json
from fsent.beans import UserBean

login_manager = LoginManager()
login_manager.init_app(app)

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    # if form.validate_on_submit():
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is not None:
                login_user(user)
                userbean = UserBean(user.id, user.username, user.email)
                # userinfo = json.dumps(userbean, cls=UserJSONEncoder)
                # session["user"] = user
                # username = user.username
                # user2 = session.get('user')
                # userinfo = json.dumps(user)
                # print(userinfo)
                # return render_template('login.html', form=form, error=error)
                return render_template('action_list.html', user=userbean)
                # return render_template('profile.html', user=user)
            else:
                error = 'User is not exist!'
            # if user is not None and bcrypt.check_password_hash(
            #     user.password, request.form['password']
            # ):
            #     login_user(user)
                flash('You were logged in. Go Crazy.')
            # return redirect(url_for('index'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('users.login'))




@login_manager.user_loader
def load_user(username):
    # Load user object from your database or other storage system
    return User.query.get(username)


# @users_blueprint.route('/register/', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User(
#             name=form.username.data,
#             email=form.email.data,
#             password=form.password.data
#         )
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         return redirect(url_for('home.home'))
#     return render_template('register.html', form=form)
