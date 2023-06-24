from abc import ABCMeta


class IPerson(metaclass=ABCMeta):

    @classmethod
    def person_method(cls):
        """Interface method"""


class Student(IPerson):

    def __init__(self):
        self.name = "Base Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print('I am a teacher')


class Programmer(IPerson):

    def __init__(self):
        self.name = "Basic Programmer Name"

    def person_method(self):
        print('I am a programmer')


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        if person_type == "Programmer":
            return Programmer()
        raise ValueError("Invalid Type")


if __name__ == "__main__":
    try:
        choice = input("What type of person do you want to create?\n")
        person = PersonFactory.build_person(choice)
        person.person_method()
    except Exception as ex:
        print(ex)
