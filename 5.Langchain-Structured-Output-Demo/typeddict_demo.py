from typing import TypedDict

class Person(TypedDict):

    name: str
    age:  int

newPerson: Person = {'name': 'Hamza', 'age': 35}

print(newPerson)