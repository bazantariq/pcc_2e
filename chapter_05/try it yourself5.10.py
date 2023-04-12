current_users = ['Jhon', 'Ali', 'Sana', 'Ahamad', 'Abbas']
new_users = ['Jhon', 'Ali', 'Sara', 'Aimen', 'Sabir']
for newuser in new_users:
    if newuser in current_users:
        print("you have to enter a new username")
    else:
        print("this user name is available")
