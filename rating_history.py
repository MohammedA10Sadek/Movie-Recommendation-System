# this function contains get_rating, rate_history, rate movie and the main function rate_and_history that calls all the
# above

def get_rating(prompt):
    while True:
        rating = int(input(prompt))
        if 0 <= rating <= 10:
            return rating
        print("Please enter a rating between 0 and 10.")


rating_history = []


def rate_history():
    # display rating history
    print("\nYour rating history:")
    for entry in rating_history:
        print(f"{entry['movie']}: {entry['rating']} Comment: {entry['comment']}")
    return None


def rate_movies():
    # Allow the user to choose between detailed rate and general rate to a movie.
    # and save it to a list
    movie = input("What movie would you like to rate? ")
    rating_type = input("Would you like to give a general or specific rating? (Enter 'general' or 'specific') ")
    if rating_type.lower() == 'general':
        rating = get_rating(f"What rating would you give {movie} out of 10? ")
        comment = input("Would you like to add a comment to your rating? (Enter 'yes' or 'no') ")
        if comment.lower() == 'yes':
            comment_text = input("Please enter your comment: ")
        else:
            comment_text = ""
        print(f"Thank you for rating {movie} a {rating} out of 10!")
        rating_history.append({'movie': movie, 'rating': rating, 'comment': comment_text})
    else:
        story = get_rating("Rate the story of the movie out of 10: ")
        characters = get_rating("Rate the characters of the movie out of 10: ")
        music = get_rating("Rate the music of the movie out of 10: ")
        acting = get_rating("Rate the acting of the movie out of 10: ")
        cinematography = get_rating("Rate the cinematography of the movie out of 10: ")
        avg_rating = (story + characters + music + acting + cinematography) / 5
        comment = input("Would you like to add a comment to your rating? (Enter 'yes' or 'no') ")
        if comment.lower() == 'yes':
            comment_text = input("Please enter your comment: ")
        else:
            comment_text = ""
        print(f"Thank you for rating {movie}! The average specific rating is {avg_rating} out of 10.")
        rating_history.append({'movie': movie, 'rating': avg_rating, 'comment': comment_text})
    return None

def rate_and_history():
    # this function is the main function that asks the user between display history or rate movies
    while True:
        action = input("Would you like to rate a movie or view your rating history? (Enter 'rate' or 'history') ")
        if action.lower() == 'history':
            rate_history()
        elif action.lower() == 'rate':
            rate_movies()
