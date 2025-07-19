from model import User

users_list = [
    User("admin", "flvby", 'Михаил Ануфрев'),
    User("Jame22", 'myaw123', "Джейм Джонс"),
    User("GhostRunner1", 'rieltor556x', "Саша Дариев"),
]

users_dict = {user.login: user for user in users_list}
# {
#     'admin': User("admin", "flvby", 'Михаил Ануфрев'),
#     ...
# }

def get_user_by_login(login):
    return users_dict.get(login)
    # return users_dict[login]

