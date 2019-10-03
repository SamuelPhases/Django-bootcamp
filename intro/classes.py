class Animal:
    name = 'Cheetah'

    def eat(self):
        print('All Animals Eat')

    def run(self):
        print('All Animals can run')

mammal = Animal()
mammal.eat()


class Animals:

    # Constructor
    def __init__(self, name1):
        self.name = name1


    def eat(self):
        print("The {} can eat".format(self.name))

    def run(self):
        print('All Animals can run')

    def active(self):
        print("All Animals are active")

mammal = Animals("Dog")
mammal.eat()

