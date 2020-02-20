
DAYS = 
LIBRARIES = set()
BOOKS = set()

def setup(): 
    pass


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

class Library:
'''
    Contains an index, a set() of books, and the integer throughput and 
    signup time for the Library.
'''
    def __init__(self, index, books, throughput, signup_time):
        self.index = index
        self.books = books
        self.throughput = throughput
        self.signup_time = signup_time

        #  Order the books by score (decreasing) for ease of use.
        self.books.sort(key=lambda b: b.score, reverse=True)

class Book:
'''
    Contains an index and score for a Book.
'''
    def __init__(self, index, score):
        self.index = index
        self.score = score


