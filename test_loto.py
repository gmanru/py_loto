from loto import Player
from loto import CardGame


def test_generator():
    imit_generator = [[59, 22, '--', 36, 62, '--', 39, '--', '--'], [51, '--', '--', 57, 16, 63, '--', 4, '--'], ['--', 74, 61, 24, 83, '--', '--', 44, '--']]
    assert Player.generate_card() != imit_generator
    assert type(Player.generate_card()) == type(imit_generator)
    assert len(Player.generate_card()) == len(imit_generator)

def test_barrels():
    imit_checklist = [x for x in range(90)]
    assert CardGame.barrel_number(imit_checklist) != CardGame.barrel_number(imit_checklist)
    