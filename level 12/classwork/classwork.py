def register():
    username = input(" ")
    password = input("")
    confirm_password = input(" ")

    age = int(input(" "))

    if len(username) < 5:
        print("")
    elif len(password) < 8:
        print("")
    elif password != confirm_password:
        print("")
    elif age < 18:
        print("")
    else:
        print(f"{username}!")
register()