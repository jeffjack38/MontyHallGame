class Person:
    """Person class"""
    def __init__(self, fname, lname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not(name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self._last_name = lname
        self._first_name = fname



    def display(self):
        return self._first_name + ", " + self._last_name


