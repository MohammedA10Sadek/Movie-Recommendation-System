import csv


def display_top_movies():
    while True:
        top_num = input('-To what number do you want in list of top movies(from 1 to 100): ')
        top_num = top_num.replace(" ", "")
        if top_num.isdigit() and 1 <= int(top_num) <= 100:
            break
        elif not top_num.isdigit():
            print("Invalid input. Please try again")
        else:
            print("Invalid number. Please try again")

    with open('movies.csv', 'r') as top_folder:
        Top_movies = csv.DictReader(top_folder)
        count = 0
        print('\n')
        for row in Top_movies:
            if count >= int(top_num):
                break
            count += 1
            print(row['movie_name'], row['year_of_release'], ',Rating:', row['imdb_rating'])
        print('\n')

    contain = input('-Do you want to see detailed information about them?(yes or no): ')
    contain = contain.replace(" ", "").lower()
    if contain == 'yes':
        with open('movies.csv', 'r') as top_folder_2:
            Top_movies_2 = csv.reader(top_folder_2)
            count = 0
            next(top_folder_2)
            print('\n')
            for row in Top_movies_2:
                if count >= int(top_num):
                    break
                count += 1
                print(', '.join(row))
            print('\n')
    else:
        print('Thank you for using our program :)🤍')
        return
