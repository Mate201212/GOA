def register():
    
    username = input("): ")
    
    # მომხმარებლის პაროლი
    password = input("): ")
    
    confirm_password = input(" ")

    # მომხმარებლის ასაკი
    age = int(input(""))

    # რეგისტრაციის ლოგიკა
    if len(username) < 5:
        print("")
    elif len(password) < 8:
        print("")
    elif password != confirm_password:
        print("")
    elif age < 18:
        print("")
    else:
        print(f", {username}!")


register()
