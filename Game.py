import Game
import CarPlayer


class Game:
    def __init__(self):
        self.__players = []
        self.__rounds = 0

    def init(self):
        self.__players = []
        playerNames = input("이름을 입력해주세요: .(이름은쉼표(,)기준으로구분)").replace(" ", "")
        playerNamesContainer = playerNames.split(',')

        while(len(playerNamesContainer) != 0):
            player = CarPlayer.Car(playerNamesContainer.pop())
            self.__players.append(player)

        self.__rounds = int(input("몇 회 하시겠습니까?: "))

    def play(self):
        while(self.__rounds > 0):
            self.__rounds -= 1
            players = self.__players
            for player in players:
                player.play()

    def printState(self):
        players = self.__players
        for player in players:
            print(player)
