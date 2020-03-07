# CarGame.py

import random

class Car():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def play(self):
        randomNumber = random.randint(0, 9)
        if randomNumber >= 4:
            self.position = self.position + 1
            return self.position

        else: return self.position




try_ = 0
carName = input("이름을 입력해주세요: ").replace(' ', '')
repeat = int(input("몇 회 하시겠습니까?: "))
carName = carName.split(',')
newList = []

for i in carName:
    i = Car(i, 0)
    for try_ in range(repeat):
        i.play()

    print(i.name, ':', '-' * i.position)

'''
    newList.append(i.position)
    print(i)
print(newList)
'''
