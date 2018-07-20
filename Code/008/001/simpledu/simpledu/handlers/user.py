from flask import Blueprint,render_template,abort
from simpledu.models import User,Course

user = Blueprint('user', __name__, url_prefix='/user/<username>')


@user.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@user.route('/')
def user_index(username):
    users = User.query.filter_by(username=username).first()
    if not users:
        abort(404)
    courses = Course.query.filter_by(author_id=users.id)

    return render_template('user.html', users=users,courses=courses)
