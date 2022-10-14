
class Person:
    def __init__(self):
        self.name : name
        self.surname : surname
        self.birthyear : birthyear

    def breathing(self):
        return ("You are breathing")

    def walking(self):
        return ("You are walking")


myself = Person()
print(myself.walking())