from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
# from flask.ext.login import login_user, login_required, logout_user

from .forms import LoginForm
from fsent import db
from fsent.models import User

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         user = User.query.filter_by(name=request.form['username']).first()
    #         if user is not None and bcrypt.check_password_hash(
    #             user.password, request.form['password']
    #         ):
    #             login_user(user)
    #             flash('You were logged in. Go Crazy.')
    #             return redirect(url_for('home.home'))

    #         else:
    #             error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)