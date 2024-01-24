from dbModels import *
from pony.orm import *

USER_SCHEMA = {
    "name": 'test',
    "password": "<PASSWORD>",
    "username": "test@123"
}


@db_session
def create_user(userdata):
    try:
        u1 = User(name=userdata.name, password=userdata.password, username=userdata.username)
        return f"User Created! {u1.username}"

    except Exception as e:
        return f"Error: {e}"


@db_session
def get_user(username):
    try:
        userdetail = User.get(username=username)
        return userdetail.name
    except Exception as e:
        return f"Error: {e}"


@db_session
def check_password(username, password):
    try:
        userdetail = User.get(username=username)
        if userdetail.password == password:
            return True
        else:
            return False
    except Exception as e:
        return f"Error: {e}"


@db_session
def delete_user(username):
    try:
        userdetail = User.get(username=username)
        userdetail.delete()
        return True
    except Exception as e:
        return f"Error: {e}"

