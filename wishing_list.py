
def wishing_list ():
    user_data_file = 'user_data.txt'
    user_data = {}

    #Read the user data from the file and add it to the user_data dictionary
    with open(user_data_file, 'r') as f:
        for line in f:
            username, password, watched_list, wishing_list, *extra = line.strip().split('-')
            user_data[username] = {'password': password, 'watched_list': watched_list, 'wishing_list': wishing_list}

    #Loop to get user credentials and check if they are valid
    while True:
        username = input("Please for security, sign in again with Enter the username: ")
        password = input("Please, Enter your password: ")

        # Check if the user is in the user_data dictionary and the password is correct
        if username in user_data and user_data[username]['password'] == password:
            print("Logging in...")
            print(f'Welcome back, {username}!')
            # If the credentials are valid, retrieve the user's watched list
            wishing_list = user_data[username]['wishing_list']
            print("Your watched list:", wishing_list)

            # Loop to ask the user if they want to add a movie to their watched list
            while True:
                add_to_wishing_list = input('Do you want to add a movie to your wishing list?(yes/no): ')
                add_to_wishing_list = add_to_wishing_list.replace(" ", "").lower()
                if add_to_wishing_list == 'yes' or add_to_wishing_list == 'no':
                    break
                elif add_to_wishing_list.isdigit():
                    print('invalid input, Please Try again with yes or no only')
                else:
                    print('invalid input, Please try again with yes or no')
            if add_to_wishing_list == "no":
                print('Thank you for using our program :)🤍\n')
                print("Logging out...")
                break

            # Prompt the user to enter the name of the movie(s) they want to add to their watched list
            new_movie = input("Enter a movie "
                              "(if it is more than two movies, separate it with ',')"
                              " to add to your wishing list: ").split(',')
            # Add the new movie(s) to the user's watched list
            movies = ','.join(new_movie)
            wishing_list = wishing_list + f', {movies}'
            user_data[username]['wishing_list'] = wishing_list
            print('your updated wishing list is: ', user_data[username]['wishing_list'])
            # Write the updated user data back to the file
            with open(user_data_file, 'w') as f:
                for username, data in user_data.items():
                    password = data['password']
                    wishing_list = data['wishing_list']
                    f.write(f"{username}-{password}-{watched_list}-{wishing_list}\n")
            while True:
                repeat_again = input('\nDo you want to contain?(yes/no): ')
                repeat_again = repeat_again.replace(" ", "").lower()
                if repeat_again == 'yes' or 'no':
                    break
                elif repeat_again.isdigit():
                    print('invalid input, Please Try again with yes or no only')
            if repeat_again == "no":
                print('Thank you for using our program :)🤍\n')
                print("Logging out...")
                break
        else:
            print("Invalid username or password.")
    return None
