
def powerset(s):
    """
    Generate powerset
    :param s: The set
    :return: The powerset
    """
    ps = [[]]
    for e in s:
        ps.extend([ss + [e] for ss in ps])
    return ps


def ps_books(libs):
    """
    Takes a library and returns the powerset of the books
    including the cardinality, fitness
    :param libs: List of libraries
    :return: The powerset of libraries
    """
    pass
