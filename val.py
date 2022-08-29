from Person import Person


class Personer(Person):
    def __init__(self, persons_list):
        self.persons_list = persons_list
        self.val ={person.pnum:person.val for person in persons_list}
        print(self.val)
    def check_duplicate(self):
        pnums = []