from pony.orm import Database, Required, Set, db_session

db = Database(
    provider='mysql',
    host='34.229.160.16',
    user='root',
    passwd='Password@123',
    db='temp_db'
)

#
# class User(db.Entity):
#     username = Required(str, unique=True)
#     name = Required(str, unique=True)
#     password = Required(str)
#
#
#
# db.generate_mapping(create_tables=True)
#

# @db_session
# def create_entity():
#     u1 = User(name='test', password='123', username='test@123')
#
#
# @db_session
# def get_entity(uname):
#     userdetail = User.get(username=uname)
#     return userdetail.name
#         # return user
#
#
# # print(create_entity())
# print(get_entity('test@123'))
