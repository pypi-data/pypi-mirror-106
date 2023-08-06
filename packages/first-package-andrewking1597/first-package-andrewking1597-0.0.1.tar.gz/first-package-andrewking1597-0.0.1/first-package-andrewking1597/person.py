class Person:
    def __init__(self, name='friend', age=18, gender='male'):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce_self(self):
        return "Hi! My name is {} and I'm {} years old.".format(self.name, self.age)

    def say_goodbye(self, name=None):
        if name:
            return "Goodbye, {}!".format(name)
        else:
            return "Goodbye!"