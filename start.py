import user


# this function import user file which contain sign_in and sign_guest functions which call the rest of features based on
# the type of user if he logged in or signed in as a guest.

def user_acc(acc):
    # Allow users to choose between signing in to their account or signing in as a guest with limited features.
    # MAke sure that  username and password are correct
    x = 'sign in'
    y = 'guest'
    if acc == x:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        with open('login.txt', 'r') as f:
            login_info = f.readline().strip().split(',')
        # strip any empty space and read the line then separate the username and password strings
        # Check if the username and password are correct
        if username == login_info[0] and password == login_info[1]:
            print('You signed in to your account successfully')
            user.sign_in()
            # calls sign_in function from user file
            return acc
        else:
            print('Incorrect username or password')
            return None

    elif acc == y:
        print('You signed in as a guest')
        print('As a guest, you only have access to the search bar, top movies, and recommendation system')
        user.sign_guest()
        # calls sign_guest function from user file
        return acc

    else:
        print('Invalid option')
        return None
