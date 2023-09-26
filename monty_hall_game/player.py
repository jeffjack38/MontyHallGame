#derived class

from person import Person


class Player(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        player_id_characters = set("1234567890")
        if not player_id_characters.issuperset(id):
            raise ValueError
        self.id = id

    def display(self):
        return str(self._first_name + " " + self._last_name + ": " + str(self.id))


my_player = Player('Jack', 'Aden', "1")
print(my_player.display())
