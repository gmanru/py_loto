from loto import Player, CardGame

imit_checklist = [x for x in range(91)]
TestPlayer = Player()
imit_generator = [[59, 22, '--', 36, 62, '--', 39, '--', '--'], [51, '--', '--', 57, 16, 63, '--', 4, '--'], ['--', 74, 61, 24, 83, '--', '--', 44, '--']]


def test_generator():
    assert TestPlayer.card != Player.generate_card() != imit_generator
    assert type(Player.generate_card()) == type(imit_generator) == type(TestPlayer.card)
    assert len(Player.generate_card()) == len(imit_generator) == len(TestPlayer.card)


def test_barrels():
    assert CardGame.barrel_number(imit_checklist) != CardGame.barrel_number(imit_checklist)
