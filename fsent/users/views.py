from flask import flash, redirect, render_template, request, url_for, Blueprint, session, jsonify
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

@users_blueprint.route('/', methods=['GET', 'POST'])
@users_blueprint.route('/ulogin', methods=['GET', 'POST'])
def ulogin():
    error = None
    form = LoginForm(request.form)
    # if form.validate_on_submit():
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is not None:
                login_user(user)
                userbean = UserBean(user.id, user.username, user.email)
                return render_template('action_list.html', user=userbean)
            else:
                error = 'User is not exist!'
                flash('You were logged in. Go Crazy.')
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/loginj', methods=['GET', 'POST'])
def loginJ():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is not None:
                login_user(user)
                userbean = UserBean(user.id, user.username, user.email)
                return jsonify({"status":"200", "msg": "", "data" : userbean.to_dict})
            else:
                error = 'User is not exist!'
        else:
            error = 'Invalid username or password.'
    return jsonify({"status":"400", "msg": error})



@users_blueprint.route('/ulogout', methods=['GET', 'POST'])
@login_required
def ulogout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('users.ulogin'))


@login_manager.user_loader
def load_user(username):
    # Load user object from your database or other storage system
    return User.query.get(username)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    item = request.get_json()
    user = User.query.filter_by(username=item['username']).first()
    if user is None:
        error = 'User is not exist!'
        return jsonify({"status":"400", "msg": error})
    elif (user.password != item['password']):
        error = 'Invalid username or password.'
        return jsonify({"status":"400", "msg": error})
    else:
        return jsonify({"status":"200", "msg": "", "data" : user.to_dict()})


    # error = None
    # form = LoginForm(request.form)
    # # if form.validate_on_submit():
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         user = User.query.filter_by(username=request.form['username']).first()
    #         if user is not None:
    #             login_user(user)
    #             userbean = UserBean(user.id, user.username, user.email)
    #             return jsonify({"status":"200", "msg": "", "data" : userbean.to_dict()})
    #         else:
    #             error = 'User is not exist!'
    #     else:
    #         error = 'Invalid username or password.'
    # return jsonify({"status":"400", "msg": error})

@users_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"status":"200", "msg": "User logout!"})