from hashcode_shared import *

from random import shuffle

FILEPATH = "datasets/b_read_on.txt"

NUM_DAYS = 0  
NUM_BOOKS = 0
NUM_LIBRARIES = 0

LIBRARIES = []
BOOKS = []

def setup(): 
    '''
    Loads the data from the inital file (FILEPATH)
    '''
    global NUM_DAYS, NUM_BOOKS, NUM_LIBRARIES
    global BOOKS, LIBRARIES

    with open(FILEPATH, 'r') as f:
        #  Load the number of days, libraries, and books.
        line_1 = f.readline()
        split_line_1 = line_1.split(" ") 
        NUM_BOOKS = int(split_line_1[0])
        NUM_LIBRARIES = int(split_line_1[1])
        NUM_DAYS = int(split_line_1[2])

        #  Load in the Books
        line_2 = f.readline() 
        split_line_2 = line_2.split(" ")
        for index, score in enumerate(split_line_2):
            #  Create a Book object given the score, and the index
            book = Book(index, int(score))
            BOOKS.append(book)

        #  Load in the Libraries
        for i in range(0, NUM_LIBRARIES * 2, 2):
            #  line i contains => #books  signup_time  throughput 
            line_i = f.readline() 
            split_line_i = line_i.split(" ")
            signup_time = int(split_line_i[1])
            throughput = int(split_line_i[2])


            #  line i+1 contains list of books (space separated)
            library_books = []
            line_i_plus_1 = f.readline()
            split_line_i_plus_1 = [int(j) for j in line_i_plus_1.split(" ")]

            #  Put all of the Books into the Library's list
            for j in split_line_i_plus_1:
                library_books.append(BOOKS[j])

            library = Library(i//2, library_books, throughput, signup_time)
            LIBRARIES.append(library)

def get_all_books():
    '''
        Get the list of all books available (i.e. BOOKS before we
        cut it up).
    '''
    full_set = set() 
    book_sets = {set(l.books) for l in LIBRARIES}
    for book_set in book_sets:
        full_set.union(book_set)
     
    return full_set

def heuristic(days_left, library):
    '''
        Calculates the maximum score a library will obtain with
        some number of days left
    '''
    global BOOKS

    #  We have this much less time overall
    days_left -= library.signup_time     

    #  Take the maximum number of books we can scan in the time left
    max_taken = days_left * library.throughput

    #  Calculate the score by taking all of the best books. 
    #  Don't choose any that have already been scanned.
    chosen_books = [b for b in library.books[:max_taken] if b in BOOKS]
    chosen_books_scores = [b.score for b in chosen_books]
    score = sum(chosen_books_scores)

    return (chosen_books, score)

def greedy_schedule(): 
    global BOOKS
    global LIBRARIES

    signup_schedule = [] 
    scanning_schedule = []

    #  Work through the days.
    for d in range(NUM_DAYS):
        print("[SCHEDULING] DAY {}".format(d))

        #  If there are no more libraries, quit
        if len(LIBRARIES) == 0:
            break

        #  If no more libraries can be scheduled, we're done.
        if max([l.signup_time for l in LIBRARIES]) > NUM_DAYS - d:
            break

        #  Calculate the maximum scores for each Library
        scores = [(l, heuristic(NUM_DAYS - d, l)) for l in LIBRARIES]

        #  Choose the Library (and corresponding set of Books) that generate
        #  the maximum score.
        sorted_choices = sorted(scores, key=lambda c: c[1][1], reverse=True)
        top_choice = sorted_choices[0]

        top_library = top_choice[0]
        top_books = top_choice[1][0]

        #  Add the best library to the signup_schedule
        signup_schedule.append(top_library)

        #  Add the corresponding books to the scanning_schedule
        scanning_schedule.append(top_books)

        #  Remove the chosen Books from BOOKS
        for book in top_books:
            BOOKS.remove(book)

        #  Remove the chosen Library from LIBRARIES
        LIBRARIES.remove(top_library)

        #  Elapse the correct number of days...
        d += top_library.signup_time

    return zip(signup_schedule, scanning_schedule)  


def output(schedule):
    print("{}".format(len(schedule)))
    for choice in schedule:
        print("{} {}".format(choice[0].index, len(choice[1])))
        print(" ".join([str(b.index) for b in choice[1]]))

if __name__ == "__main__":
    setup() 
    schedule = list(greedy_schedule())
    output(schedule) 
