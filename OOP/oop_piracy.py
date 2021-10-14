# https://www.codewars.com/kata/54fe05c4762e2e3047000add/python

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20


if __name__ == '__main__':
    Titanic = Ship(15, 10)
    print(Titanic.is_worth_it())
