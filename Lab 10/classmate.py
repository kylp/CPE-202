"""contains Classmate class and its factory function

CPE202 Winter 2020
"""
class Classmate:
    """class for Classmate

    Attributes:
        sid (int) : id
        last (str) : last name
        first (str) : first name
        major (str) : major
        year (str) : year
    """
    def __init__(self, sid, last, first, major, year):
        self.sid = sid
        self.last = last
        self.first = first
        self.major = major
        self.year = year

    def __repr__(self):
        return "Classmate{sid: %d, last: %s, first: %s, major: %s, year: %s}"\
            % (self.sid, self.last, self.first, self.major, self.year)

    def __eq__(self, other):
        return isinstance(other, Classmate)\
            and self.sid == other.sid\
            and self.last == other.last\
            and self.first == other.first\
            and self.major == other.major\
            and self.year == other.year


def classmate_factory(tokens):
    """Create a Classmate object by parsing tokens

    Args:
        tokens (list) : a list of str
                        The second item contains the name but in last, first format.
    Returns:
        Classmate : a Classmate object
    """
    sid = int(tokens[0])
    name_parts = tokens[1].split(',')
    last = name_parts[0].strip()
    first = name_parts[1].strip()
    major = tokens[2]
    year = tokens[3].strip('\n')
    return Classmate(sid, last, first, major, year)
