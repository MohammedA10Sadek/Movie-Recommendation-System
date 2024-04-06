import watching_list
import wishing_list
import Search
import summary
import displaytopmovies
import rating_history
import recommendd

# this file contain sign_in and sign_guest functions
# those functions calls another functions based on user choice
# ofcourse if the user enter as a guest the function sign_guest will provide limited features


def sign_in():
    while True:
        choice_display = input(
            '-What section do you want to see(1.display, 2.rate or show rating history, 3.recommend movies): ')
        choice_display = choice_display.replace(" ", "")
        if choice_display.isdigit() and 1 <= int(choice_display) <= 5:
            break
        elif not choice_display.isdigit():
            print("Invalid input. Please try again with a number only: ")
        else:
            print("Invalid number. Please try again")

    if int(choice_display) == 1:
        display = input(
            'What do you want to display? \ntype "1" for watching list \ntype "2" for wishing list \ntype"3" for search engine \ntype"4" to display top movies \ntype "5" to display summary from other users about a movie')
        if display == '1':
            watching_list.watching_list()
        elif display == '2':
            wishing_list.wishing_list()
        elif display == '3':
            Search.search_engine()
        elif display == '4':
            displaytopmovies.display_top_movies()
        elif display == '5':
            summary.display_summary()
    elif int(choice_display) == 2:
        rating_history.rate_and_history()
    elif int(choice_display) == 3:
        movie_title =input('Enter movie title')
        print(recommendd.recommend_movies(movie_title))
    return None


def sign_guest():
    # This functions provides access to limited features to the user
    display_guest = input(
        'To access to: \n1- search bar press (1) \n2- recommend a movie press (2) \n3-Show Top Movies press (4)')
    if display_guest == '1':
        Search.search_engine()
    elif display_guest == '2':
        movie_title = input('Enter movie title')
        print(recommendd.recommend_movies(movie_title))
    elif display_guest == '3':
        displaytopmovies.display_top_movies()
    return None