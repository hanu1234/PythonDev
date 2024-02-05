from abc import ABC, abstractmethod


class Animal(ABC):

    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def sound(self):
        pass


class Dog(Animal):
    def __int__(self):
        print("This dog is crazy dog")


obj = Dog()
obj.eat()
