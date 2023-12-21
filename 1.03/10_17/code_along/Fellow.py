# TODO: implement Fellow class that inherits from "Person"
# we just include another method called "form_group()"
# that prints out all the people that this fellow knows
from Person import PersonClass
# using a for-loop. Implement below


class Fellow(PersonClass) :

    def form_group(self):
        for name in self.aff:
         print(name)


fellowA= Fellow("Bob", "Plov", ["Mo", "Ken"])

print(fellowA.name)
fellowA.form_group()
