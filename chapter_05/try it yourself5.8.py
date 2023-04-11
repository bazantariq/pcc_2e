user_names = ['admin', 'Jhon', 'Ali', 'Sana', 'Ahamad', 'Abbas']
for eachuser in user_names:
    if eachuser == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+eachuser+", thankyou for logging in again")
        