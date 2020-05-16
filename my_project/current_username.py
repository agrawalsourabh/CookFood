from flask_login import login_required, current_user
from my_project.sign_up.models import UserInfo

def user_name():
    userinfo = UserInfo.query.filter_by(email=current_user.email).first()
    return userinfo.profile_image