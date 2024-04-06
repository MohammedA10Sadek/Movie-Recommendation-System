import csv

def display_summary():
    while True:
        with open('summary.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            # Create a dictionary to store the movie reviews
            reviews = {}
            c = 0
            for row in reader:
                reviews[row[0].replace(' ', '').lower()] = (row[2], row[1])

        # Ask the user for a movie title
        movie = input('Enter a movie title: ')
        movie = movie.replace(' ', '').lower()

        # Check if the movie is in the reviews dictionary
        if movie in reviews:
            # Print the review for the movie
            print(f'User name: {reviews[movie][0]}\nhis/her rating: \n{reviews[movie][1]}')
        else:
            # Print an error message if the movie is not found
            print('Sorry, the movie you searched for is not found. Please enter another movie.')
        while True:
            print('\n')
            repeat = input('Do you want to see another review from ather users?(Y/N): ')
            repeat = repeat.replace(" ", "").lower()
            if repeat == 'yes' or 'no':
                break
            elif repeat.isdigit():
                print('invalid input, Please Try again')
            else:
                print('invalid input, Please try again')
        if repeat == 'no':
            break
    return None
