import random
from random import randrange
import  pprint
class Card:
    @staticmethod
    def generate_card():

        # создаем структуру билета лото
        dx = 9
        dy = 3
        structure = [[0 for x in range(dx)] for y in range(dy)]

        # генерируем рандомные значения бочонков в билете

        random_values = []
        while len(random_values) < 16:
            new_num = randrange(1, 90, 1)
            if new_num not in random_values:
                random_values.append(new_num)

        numbers_1 = []
        while len(numbers_1) < 5:
            new_num = randrange(0, 8, 1)
            if new_num not in numbers_1:
                numbers_1.append(new_num)

        numbers_2 = []
        while len(numbers_2) < 5:
            new_num = randrange(10, 18, 1)
            if new_num not in numbers_2:
                numbers_2.append(new_num)

        numbers_3 = []
        while len(numbers_3) < 5:
            new_num = randrange(20, 28, 1)
            if new_num not in numbers_3:
                numbers_3.append(new_num)

        numbers_result = numbers_1 + numbers_2 + numbers_3

        for x in range(3):
            for y in range(9):
                index = str(x) + str(y)
                if index[0] == "0":
                    index = index[1]

                if int(index) in numbers_result:

                    structure[x][y] = random_values.pop()
                else:

                    structure[x][y] = "--"

        return structure

    @staticmethod
    def bochonok_number(spisok):

        new_num = randrange(1, len(spisok), 1)

        return spisok.pop(new_num)

class Player(Card):
    def __init__(self):
        self.card = self.generate_card()

    def pretty_print_generate(self):
        print("==========Это ваша карта=============")
        for x in range(3):
            print(self.card[x])

    def _continue_game(self, num):
        check = False

        for x in range(3):
            for y in range(9):
                if self.card[x][y] == num:
                    self.card[x][y] = "--"
                    check = True
        if check == False:

            return True
        else:
            return "False"

    def _delete_card(self,num):
        check = False

        for x in range (3):
            for y in range(9):
                if self.card[x][y] == num:
                    self.card[x][y] = "--"
                    check = True
        if check == True:

            return self.card
        else:
            return "False"





class Human(Player):
    def __init__(self):
        self.card = self.generate_card()

    def human_action_del(self,num):

            if self._delete_card(num) == "False":

                return "error"

            else:
                return self._delete_card(num)

    def human_action_cont(self, num):

        if self._continue_game(num) == "False":

            return "error"

        else:
            return "right"


class Computer(Player):
    def __init__(self):
        self.card = self.generate_card()


    def action_robo(self,num):

        if self._delete_card(num)=="False":
            print("компьютер решил продолжить игру")
            return self._continue_game(num)
        else:
            print("компьютер решил зачеркнуть бочонок")
            return self._delete_card(num)







human_1 = Human()
robot_1 = Computer()
card_1 =Card()





spisok_bochonkov = [x for x in range(90)]

while True:
    bochonok_1 = card_1.bochonok_number(spisok_bochonkov)
    human_1.pretty_print_generate()
    print(f"========Выпало число {bochonok_1}============")
    answer = input("Зачеркнуть или продолжить? y/n ?")
    print("==============================================")
    robot_1.action_robo(bochonok_1)
    if answer == "y":
        if human_1.human_action_del(bochonok_1) != "error":
            continue
        else:
            print("Конец игры!!!")
            break
    elif answer == "n":
        if human_1.human_action_cont(bochonok_1) != "error":
            continue
        else:
            print("Конец игры!!!")
            break
