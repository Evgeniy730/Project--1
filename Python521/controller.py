import user_db

def auth_user(login, password):
    user = user_db.get_user_by_login(login.strip())
    
    if user == None:
        message = "Пользователя с таким логином не существует!"
    elif user.is_correct_password(password.strip()):
            message = "Привет " + user.initials
    else:
        message = "Указан неверный пароль!"

    print(message)
