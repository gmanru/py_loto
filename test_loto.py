from random import randrange


def generate_card():
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


def test_generator():
    imit_generator = [[59, 22, '--', 36, 62, '--', 39, '--', '--'], [51, '--', '--', 57, 16, 63, '--', 4, '--'], ['--', 74, 61, 24, 83, '--', '--', 44, '--']]
    assert generate_card() != imit_generator
    assert type(generate_card()) == type(imit_generator)
    assert len(generate_card()) == len(imit_generator)


checklist = [x for x in range(90)]


def barrel_number(checklist):

        new_num = randrange(1, len(checklist), 1)

        return checklist.pop(new_num)


def test_barrels():
    testlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
    assert checklist == testlist
    assert barrel_number(checklist) != barrel_number(testlist)
