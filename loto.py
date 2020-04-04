from random import randrange


class CardGame:

    @staticmethod
    def barrel_number(checklist):
        print(checklist)
        new_num = randrange(1, len(checklist), 1)
        print(checklist.pop(new_num))

        return checklist.pop(new_num)

    @staticmethod
    def win(checklist):
        i = 0
        for x in range(3):
            for y in range(9):
                if str(checklist[x][y]).isdigit() is True:
                    i += 1
        if i == 0:
            return "win"


class Player:
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
        if check is False:

            return True
        else:
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
            return False


class Human(Player):

    def _delete_card(self, num):
        result = super()._delete_card(num)
        return "error" if not result else result

    def _continue_game(self, num):
        result = super()._continue_game(num)
        return "error" if not result else result


class Computer(Player):

    def _delete_card(self, num):
        if(super()._delete_card(num)):
            print("компьютер решил зачеркнуть бочонок")
        return super()._delete_card(num)

    def _continue_game(self, num):
        if(super()._continue_game(num)):
            print("компьютер решил продолжить игру")
        return super()._continue_game(num)


if __name__ == "__main__":
    human_1 = Human()
    robot_1 = Computer()
    card_1 = CardGame

    print("==========Добро пожаловать в игру Лото!===============")
    list_barrels = [x for x in range(91)]

    while True:
        barrel_1 = card_1.barrel_number(list_barrels)
        human_1.pretty_print_generate()
        print(f"========Выпало число {barrel_1}============")
        answer = input("Введите число 1 чтобы удалить бочонок с Вашей карточки \n Введите число 2 чтобы продолжить выбор бочонков \n")
        print("==============================================")
        robot_1._continue_game(barrel_1)
        if answer == "1":
            if human_1._delete_card(barrel_1) != "error":
                if card_1.win(human_1.card) == "win":
                    print("Ура, вы победили!!!")
                    break
                continue
            else:
                print("Вы удалили бочонок, которого не было на карте, конец игры!!!")
                break
        elif answer == "2":
            if human_1._continue_game(barrel_1) != "error":
                continue
            else:
                print("Вы продолжили игру, хотя на карте был выпавший бочонок, Конец игры!!!")
                break
