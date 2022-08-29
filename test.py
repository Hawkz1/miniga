from Person import Person
from val import Personer

Lukas = Person(pnum = '20040716-4490', val = 'Sverige Demokraterna')

print(Lukas)
persons_list = []
for i in range(10):
    persons_list.append(Person(val = 'Sverige Demokraterna', random = True))
    persons_list.append(Lukas)


J = Personer(persons_list = persons_list)