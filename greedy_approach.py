import hashcode_shared

FILEPATH = "/datasets/f_libraries_of_the_world.txt"

NUM_DAYS = 0  
NUM_BOOKS = 0
NUM_LIBRARIES = 0

LIBRARIES = set()
BOOKS = set()

def setup(): 
'''
    Loads the data from the inital file (FILEPATH)
'''
    with open(FILEPATH, 'r') as f:
        #  Load the number of days, libraries, and books.
        line_1 = f.readline()
        split_line_1 = line_1.split(" ") 
        NUM_BOOKS = split_line_1[0]
        NUM_LIBRARIES = split_line_1[1]
        NUM_DAYS = split_line[2]

        #  Load in the Books
        line_2 = f.readline() 
        split_line_2 = line_2.split(" ")
        for index, score in enumerate(split_line_2):
            #  Create a Book object given the score, and the index
            book = Book(index, score)
            BOOKS.add(book)

        #  Load in the Libraries
        

    return 


def get_all_books():
'''
    Get the set of all books available (i.e. BOOKS before we
    cut it up).
'''
    full_set = set() 
    book_sets = {l.books for l in LIBRARIES}
    for book_set in book_sets:
        full_set.union(book_set)
     
    return full_set

def heuristic(days_left, library):
'''
    Calculates the maximum score a library will obtain with
    some number of days left
'''
    #  We have this much less time overall
    days_left -= library.signup_time     

    #  Take the maximum number of books we can scan in the time left
    max_taken = days_left * library.throughput

    #  Calculate the score by taking all of the best books. 
    #  Don't choose any that have already been scanned.
    chosen_books = {b.score for b in library.books[:max_taken] if b in BOOKS}
    score = sum(chosen_books)

    return (chosen_books, score)

def schedule(): 
    pass 
