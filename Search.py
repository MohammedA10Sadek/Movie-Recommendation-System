import imdb

# creating instance of IMDb
movieBD = imdb.IMDb()


# Define a function to get the directors of a movie
def get_directors(movie):
    # Create an empty list to store the directors
    directors = []
    # Loop through each director in the 'directors' attribute
    for director in movie['directors']:
        directors.append(director['name'])
    return directors


# Define a function to get the cast of a movie
def get_cast(movie):
    cast = []
    full_cast = movie['cast']
    for person in full_cast:
        cast.append(person['name'])
    return cast


# Define a function to get some information about a movie given its ID


def get_information(movie_id):
    movie = movieBD.get_movie(movie_id)
    title = movie['title']
    rating = movie['rating']
    genre = movie['genres']
    year = movie['year']
    box_office = movie['box office']

    # call the functions of directors and cast of the movie
    directors = get_directors(movie)
    cast = get_cast(movie)

    # Return a formatted string containing the information
    return f'Movie title: {title} ({year})\nRating: {rating}\nDirector(s): {", ".join(directors)}\nCast: ' \
           f'{", ".join(cast)}\nGenre: {genre}\nBox office: {box_office}'


# Loop to allow the user to search for movies for any times and getting some information about them
def search_engine():
    while True:
        # Ask user to enter the name of the movie to search for
        ask_for_name = input('write the name of the movie fou want to search for: ')
        # Use the search_movie method of the IMDb class to search for movies with the given name
        search = movieBD.search_movie(ask_for_name)
        # numbered variable to help the user choose which movie to get information about
        c = 0
        for i in range(len(search)):
            # getting the id
            ID = search[i].movieID
            c += 1
            nnd = search[i]['title']
            # printing it
            print(f'{c}.{nnd}')

        while True:
            get_number = input('\nEnter the number shown next to the movie you want to see information about: ')
            get_number = get_number.replace(" ", "")
            if get_number.isdigit() and 1 <= int(get_number) <= c:
                break
            elif not get_number.isdigit():
                print("Invalid input. Please try again")
            else:
                print("Invalid number. Please try again")

        # we get the ID of the selected movie and use get_information function to get required information about it
        for i in range(len(search)):
            # getting the id
            ID = search[int(get_number) - 1].movieID

        print(get_information(ID))

        # Ask the user if they want to search for another movie or exit the program
        while True:
            repeat_again = input('\nDo you want to use the search again?(yes/no): ')
            repeat_again = repeat_again.replace(" ", "").lower()
            if repeat_again == 'yes' or repeat_again == 'no':
                break
            elif repeat_again.isdigit():
                print('invalid input, Please Try again with yes or no only')

        # If the user chooses to exit, print good message and break out of the loop to end the program
        if repeat_again == "no":
            print('Thank you for using our program :)🤍\n')
            break
    return None
