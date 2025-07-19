import tkinter
from config import *
from controller import auth_user

main_window = tkinter.Tk()
main_window.title(TITLE)
main_window.geometry(f'{WIDTH}x{HEIGHT}')

tkinter.Label(main_window, text="Логин").pack()
login_input = tkinter.Text(main_window, width=15, height=1)
login_input.pack()

tkinter.Label(main_window, text="Пароль").pack()
password_input = tkinter.Text(main_window, width=15, height=1)
password_input.pack()


tkinter.Button(
    main_window,
    text="Войти",
    command=lambda: auth_user(
        login=login_input.get(1.0, tkinter.END),
        password=password_input.get(1.0, tkinter.END)
    )
).pack()




main_window.mainloop()