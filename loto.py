from random import randrange


def decorate_human(f):
    def wrapper(*args, **kwargs):
        if f(*args, **kwargs) is False:

            return "error"
        else:
            return f(*args, **kwargs)

    return wrapper


def decorate_robot(f):
    def decorate_robot_inside(f1):
        def wrapper(*args, **kwargs):
            if f(*args, **kwargs):

                return f(*args, **kwargs)
            else:
                return f1(*args, **kwargs)

        return wrapper
    return decorate_robot_inside


class CardGame:

    @staticmethod
    def bochonok_number(spisok):

        new_num = randrange(1, len(spisok), 1)

        return spisok.pop(new_num)

    @staticmethod
    def win(spisok):
        i = 0
        for x in range(3):
            for y in range(9):
                if str(spisok[x][y]).isdigit() is True:
                    i += 1
        if i == 0:
            return "win"


class Player():
    @staticmethod
    def generate_card():

        # generate mass structure

        dx = 9
        dy = 3
        structure = [[0 for x in range(dx)] for y in range(dy)]

        # print(structure)

        # generate random values

        random_values = []
        while len(random_values) < 16:
            new_num = randrange(1, 90, 1)
            if new_num not in random_values:
                random_values.append(new_num)

        # print(random_values)

        # get 3 lists_indexes for 3 rows

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

        # print(numbers_1)
        # print(numbers_2)
        # print(numbers_3)
        numbers_result = numbers_1 + numbers_2 + numbers_3

        # print(numbers_result)

        for x in range(3):
            for y in range(9):
                index = str(x) + str(y)
                if index[0] == "0":
                    index = index[1]
                # print(index)

                if int(index) in numbers_result:

                    structure[x][y] = random_values.pop()
                else:

                    structure[x][y] = "--"

        return structure

    def __init__(self):
        self.card = self.generate_card()

    def pretty_print_generate(self):
        print("==========This is your card=============")
        # print(f'============== vipala cifra x ==============')
        for x in range(3):
            print(self.card[x])

    # print("======= Zacherknut cifru??   y/n =======================")

    def _continue_game(self, num):
        check = False

        for x in range(3):
            for y in range(9):
                if self.card[x][y] == num:
                    self.card[x][y] = "--"
                    check = True
        if check is False:

            return True
        else:
            # print(f'game is over(continue)({num})')
            return False

    def _delete_card(self, num):
        check = False

        for x in range(3):
            for y in range(9):
                if self.card[x][y] is num:
                    self.card[x][y] = "--"
                    check = True
        if check is True:

            return self.card
        else:
            # print(f'game is over(delete)({num})')
            return False


class Human(Player):
    def __init__(self):
        self.card = self.generate_card()

    @decorate_human
    def human_action_del(self, num):
        return self._delete_card(num)

    @decorate_human
    def human_action_cont(self, num):
        return self._continue_game(num)


class Computer(Player):

    def __init__(self):
        self.card = self.generate_card()

    def robot_delete(self, num):
        if(self._delete_card(num)) is not False:
            print("robot choise - delete")
        return self._delete_card(num)

    @decorate_robot(robot_delete)
    def action_robo(self, num):
        if(self._continue_game(num)) is not False:
            print("robot choise - continue")
        return self._continue_game(num)


human_1 = Human()
robot_1 = Computer()
card_1 = CardGame

print("==========Welcome to game===============")
spisok_bochonkov = [x for x in range(90)]

while True:
    bochonok_1 = card_1.bochonok_number(spisok_bochonkov)
    human_1.pretty_print_generate()
    print(f"========vipalo chislo {bochonok_1}============")
    answer = input("Cut or continue? y/n ?")
    print("==============================================")
    robot_1.action_robo(bochonok_1)
    if answer == "y":
        if human_1.human_action_del(bochonok_1) != "error":
            if card_1.win(human_1.card) == "win":
                print("you are win!!!")
                break
            continue
        else:
            print("game is over!!!")
            break
    elif answer == "n":
        if human_1.human_action_cont(bochonok_1) != "error":
            continue
        else:
            print(human_1.human_action_cont(bochonok_1))
            print("game is over!!!")
            break
