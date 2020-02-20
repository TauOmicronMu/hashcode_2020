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

    def __str__(self):
        return "LIBRARY({}, {}, {})".format(self.index, self.throughput, self.signup_time)

class Book:
    '''
        Contains an index and score for a Book.
    '''
    def __init__(self, index, score):
        self.index = index
        self.score = score

    def __str__(self):
        return "BOOK({},{})".format(self.index, self.score)

