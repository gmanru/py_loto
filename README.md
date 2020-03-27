# py_loto
Игра "Лото", написанная на python3.
Правила игры соответсвуют правилам из википедии https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D1%82%D0%BE
В данной игре пользователь сражается против компьютера, который всегда делает правильные действия. Единственная возможность его победить - полностью "зачеркнуть" все бочонки на карточке!
Визуально карточка выглядит так 
==========Это ваша карта=============
['--', 9, 74, 31, '--', 73, '--', 11, '--']
['--', '--', '--', 4, 48, 12, 1, 86, '--']
[14, 19, 35, '--', '--', '--', 54, 79, '--']

Ниже выводится номер бочонка из виртуального мешка
========Выпало число 60============

Далее предлагается действие на выбор:
Зачеркнуть или продолжить? y/n ?
 
Это значит либо зачеркнуть это число из карты (нажать на латинскую клавишу 'y'), либо продолжить, нажав на латинскую клавишу 'n' 

В случае, если числа не будет на карте, а вы нажмете y - то вы проиграете
Выглядеть это будет так 
Зачеркнуть или продолжить? y/n ?y
==============================================
компьютер решил продолжить игру
Конец игры!!!

Также, в случае, если выпавшее число есть на карте, а вы решите нажать n, то вы проиграли.

Праивльно выибрая когда зачеркунть, а когда пропустить, вы сможете победить компьютер. Удачи!