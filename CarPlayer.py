import random


class Car:
    def __init__(self, name):
        self.__name = name
        self.__position = 0

    def play(self):
        randomNumber = random.randint(0, 9)
        if randomNumber >= 4:
            self.__go()

    def __go(self):
        self.__position = self.__position + 1

    def __str__(self):
        return "이름: " + self.__name + "위치: " + str(self.__position)
