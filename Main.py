# Import module
import collections
import math
import os
from random import *
from tkinter import *
from tkinter import ttk, Entry, Button
from tkinter.ttk import Separator
from typing import List, Dict

# Create text file
# with open('readme.txt', 'a+') as f:
#    f.write('Create a new text file!')

# f.close()

# Create object
# root = Tk()

# Adjust size
# root.geometry("600x600")
# root.title("Title")

# set minimum window size value
# root.minsize(400, 400)

# set maximum window size value
# root.maxsize(800, 800)

# n = random.uniform(0,1)
# label = Label(root, text=n)
# label.pack()

# def callback(): global label n = random.choices([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
# 25,26,27,28,29,30,31,32,33,34,35,36], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
# k=37) ( do something lab.config(root, text=n, command=callback) ) (label.config(text=n))

# button1 = Button(root, text="Random", command=callback)

# button1.pack(ipadx=15, ipady=15, expand=True)
# button1.grid( row=5, column=5 )

# Execute tkinter
# root.mainloop()


roulette = Tk()
roulette.geometry("300x900")
roulette.title("Roulette Statistic")
roulette.minsize(320, 960)

buttons: List[Button] = list()  # Списък със бутоните на рулетката
buttons_bet: List[Checkbutton] = list()  # Списък с бутоните за залог
buttons_reset: List[Button] = list()  # Списък с бутони за отмяна на залози
red_numbers: List[int] = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers: List[int] = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
button_text: List[int] = list()  # Списък на числата върху бутоните
labels: List[Label] = list()  # Списък с числата които се отпечатват при натискане на бутоните
labels_num: List[Label] = list()  # Списък на етикетите със статистики на числата
labels_4x9_12x3: List[Label] = list()  # Списък на етикетите със статистики на групите числа
labels_18x2: List[Label] = list()  # Списък на етикетите със статистики на групите числа
buttons_calc: List[Button] = list()
lines: List[str] = list()  # Списък на Числата във файлът със статистиката като символи
stats: List[int] = list()  # Списък на Числата във файлът със статистиката
counts: List[List[int]] = [[0] * 37, [0] * 37]  # Списък от числата и броят на появата им при теглене
nine_4th_num: List[List[List[int]]] = [[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]],
                                       [[13, 16, 19, 22], [14, 17, 20, 23], [15, 18, 21, 24]],
                                       [[25, 28, 31, 34], [26, 29, 32, 35], [27, 30, 33, 36]]]
nine_4th: List[List[List[None]]] = [[[None] * 4, [None] * 4, [None] * 4],
                                    [[None] * 4, [None] * 4, [None] * 4],
                                    [[None] * 4, [None] * 4, [None] * 4]]


def n_group_2_3list(group, n):  # Записва във вторият лист броят на появата в статистиката и процентите
    a = list((math.comb(len(stats), i) * n ** i * (37 - n) ** (len(stats) - i)) for i in range(len(stats)))
    b: Dict = dict.fromkeys(group.keys(), 0)
    s: Dict = dict.fromkeys(group.keys(), 0)
    for key in group.keys():
        group[key][0] = tuple(group[key][0])
        # group[key][1] = set(group[key][1])
        b[key] = [math.comb(len(stats), group[key][2][0])]
        group[key][2] = [len(group[key][1])]
        if len(stats) > 0:  # Изчислява вероятността на получилата се комбинация в %, лист [2][1]
            group[key][2].append(round(math.comb(len(stats), group[key][2][0]) * len(group[key][0]) **
                                       group[key][2][0] * (37 - len(group[key][0])) ** (len(stats) - group[key][2][0]) *
                                       100 / (37 ** len(stats)), 2))
            # Изчислява получилата се комбинация сравнена с най-вероятната комбинация, при 1.0 съвпада, лист [2][2]
            group[key][2].append(round(math.comb(len(stats), group[key][2][0]) * len(group[key][0]) ** group[key][2][0]
                                       * (37 - len(group[key][0])) ** (len(stats) - group[key][2][0]) / max(a), 2))
            i_list: List
            i_list = []
            for i in group[key][0]:
                i_list.append(numbers37[i][2][0])
            i_list = [x for x in i_list if x != 0]
            # i_list.sort(reverse=True)
            # print(i_list)
            # print(collections.Counter(i_list))
            # Изчислява вероятността на пермутацията вътре в групата от числа, лист [2][3]
            group[key][2].append(round(math.factorial(group[key][2][0]) / math.prod(math.factorial(y) for y in i_list) *
                                       math.factorial(len(i_list)) /
                                       math.prod(math.factorial(z) for z in collections.Counter(i_list).values()) *
                                       math.comb(len(group[key][0]), len(i_list)) / len(group[key][0]) **
                                       group[key][2][0] * 100, 2))
            group[key][2].append(round(((group[key][2][0]) * 37 * 100 / (n * len(stats)) - 100), 2))
        else:
            pass

        for p in range(len(group[key][1]) - 1):  # В третият лист е броят на съседни появи в статистиката
            if group[key][1][p + 1] - group[key][1][p] == 1:
                group[key][3][0] = group[key][3][0] + 1
            else:
                pass
        for i in range(len(stats) - group[key][3][0], -1, -1):
            # Изчислява числителят на вероятностите на получилите се повторения
            s[key] = s[key] + (n ** (len(stats) - i)) * (37 - n) ** i * math.comb(abs(len(stats) - 1 - i),
                                                                                  group[key][3][0]) * math.comb(
                i + 1, len(stats) - group[key][3][0] - i)
    print(s)
    print([s[i] / 37 ** len(stats) for i in s.keys()])
    for key in group.keys():
        if len(stats) > 0:
            # Записва в речникът във третият лист на втора позиция вероятността на получилите се повторения
            group[key][3].append(round(s[key] / 37 ** len(stats) * 100, 2))
            group[key][3].append(round(group[key][3][0] * 37 * 37 * 100 / (n * n * len(stats)) - 100, 2))
        else:
            pass
    return group


def n_group_4list(group):
    for key in group.keys():  # Записва в петият [4] лист пермутацията на групата в статистиката
        if len(group[key][1]) > 0:
            for q in group[key][1][0:]:
                r = group[key][1].index(q)
                if r > 0:
                    if group[key][1][r - 1] - q == - 1:
                        group[key][4][-1] = group[key][4][-1] + 1
                    else:
                        group[key][4].extend([group[key][1][r - 1] - q + 1, 1])
                else:
                    group[key][4] = [i for i in [-q, 1] if i != 0]
                if group[key][1][-1] == q < len(stats) - 1:
                    group[key][4].append(-len(stats) + 1 + group[key][1][-1])
                else:
                    pass
        else:
            pass
    return group


numbers37: Dict[int, list] = {}


def numbers37_def():
    global numbers37, stats
    numbers37.clear()
    numbers37 = dict.fromkeys((p for p in range(37)))  # Речник с позициите на всяко число в статистиката
    for p in range(37):
        numbers37[p] = [[p]]
        # numbers37[p].extend([[[0]] * 4])
        numbers37[p].extend([[], [0], [0], [0]])
        # Третият лист е за броят на повторенията на числото в две съседни тегления
    for m in range(len(stats)):
        numbers37[stats[m]][1].append(m)
        numbers37[stats[m]][2] = [len(numbers37[stats[m]][1])]

    n_group_2_3list(numbers37, 1)
    n_group_4list(numbers37)
    print(numbers37)
    return numbers37


numbers12x3: Dict[str, list] = {}  # Речник за третините по вертикал и хоризонтал


def numbers12x3_def():  # Първата стойност е лист от позициите им в статистиката, после е броят на позициите в
    # статистиката
    global numbers12x3, stats  # Третият лист е броят на повторенията в съседни числа от статистиката
    numbers12x3.clear()
    numbers12x3 = {'1-12': [list(range(1, 13, 1))], '13-24': [list(range(13, 25, 1))],
                   '25-36': [list(range(25, 37, 1))], '1/34': [list(range(1, 37, 3))],
                   '2/35': [list(range(2, 37, 3))], '3/36': [list(range(3, 37, 3))]}
    for key in numbers12x3.keys():
        numbers12x3[key].extend([[], [0], [0], [0]])
    print(numbers12x3)
    for m in range(len(stats)):
        for key in numbers12x3.keys():
            if stats[m] in numbers12x3[key][0]:
                numbers12x3[key][1].append(m)
            else:
                pass
    n_group_2_3list(numbers12x3, 12)
    n_group_4list(numbers12x3)
    return numbers12x3


numbers4x9: Dict[tuple, list] = {}


def numbers4x9_def():
    global numbers4x9, stats  # Речник с позициите на числата комбинирани в 9 "4-ки"
    numbers4x9.clear()
    for p in range(3):  # Първият лист е позициите на "4-ката" в статистиката, вторият лист е броят й в статистиката
        for j in range(3):  # Третият лист е броят на повторенията при две съседни тегления
            # Създава речник с ключове 9 "4-ки"
            numbers4x9[tuple(nine_4th_num[p][j])] = [(nine_4th_num[p][j])]
    for q in range(9):
        numbers4x9[(1 + 4 * q, 2 + 4 * q, 3 + 4 * q, 4 + 4 * q)] = [[1 + 4 * q, 2 + 4 * q, 3 + 4 * q, 4 + 4 * q]]
    for key in numbers4x9.keys():
        numbers4x9[key].extend([[], [0], [0], [0]])
    numbers4x9[(1, 4, 7, 10)][1] = list(
        sorted(set(numbers12x3["1-12"][1]).intersection(set(numbers12x3["1/34"][1]))))
    numbers4x9[(2, 5, 8, 11)][1] = list(
        sorted(set(numbers12x3["1-12"][1]).intersection(set(numbers12x3["2/35"][1]))))
    numbers4x9[(3, 6, 9, 12)][1] = list(
        sorted(set(numbers12x3["1-12"][1]).intersection(set(numbers12x3["3/36"][1]))))
    numbers4x9[(13, 16, 19, 22)][1] = list(
        sorted(set(numbers12x3["13-24"][1]).intersection(set(numbers12x3["1/34"][1]))))
    numbers4x9[(14, 17, 20, 23)][1] = list(
        sorted(set(numbers12x3["13-24"][1]).intersection(set(numbers12x3["2/35"][1]))))
    numbers4x9[(15, 18, 21, 24)][1] = list(
        sorted(set(numbers12x3["13-24"][1]).intersection(set(numbers12x3["3/36"][1]))))
    numbers4x9[(25, 28, 31, 34)][1] = list(
        sorted(set(numbers12x3["25-36"][1]).intersection(set(numbers12x3["1/34"][1]))))
    numbers4x9[(26, 29, 32, 35)][1] = list(
        sorted(set(numbers12x3["25-36"][1]).intersection(set(numbers12x3["2/35"][1]))))
    numbers4x9[(27, 30, 33, 36)][1] = list(
        sorted(set(numbers12x3["25-36"][1]).intersection(set(numbers12x3["3/36"][1]))))
    for r in range(len(stats)):
        for key in list(numbers4x9.keys())[9:]:
            if stats[r] in key:
                numbers4x9[key][1].append(r)
            else:
                pass
            # print(key)

    n_group_2_3list(numbers4x9, 4)
    n_group_4list(numbers4x9)
    return numbers4x9


numbers18x2: Dict[str, list] = {}  # Речник за половините


def numbers18x2_def() -> object:  # Първата стойност е лист от позициите им в статистиката, после е броят на позициите в
    # статистиката
    global numbers18x2, stats  # Третият лист е броят на повторенията в съседни числа от статистиката
    numbers18x2.clear()
    numbers18x2 = {'1-18': [list(range(1, 19, 1))], '19-36': [list(range(19, 37, 1))],
                   'odd': [list(range(1, 37, 2))], 'even': [list(range(2, 37, 2))],
                   'red': [red_numbers],
                   'black': [black_numbers]}
    for key in numbers18x2.keys():
        numbers18x2[key].extend([[], [0], [0], [0]])
    for m in range(len(stats)):
        for key in numbers18x2.keys():
            if stats[m] in numbers18x2[key][0]:
                numbers18x2[key][1].append(m)
            else:
                pass

    n_group_2_3list(numbers18x2, 18)
    n_group_4list(numbers18x2)
    return numbers18x2


numbers9x4: Dict[str, list] = {}  # Речник за числата разделени на четири "9-ки" плюс odd-even/red-black


def numbers9x4_def() -> object:
    global numbers9x4, stats
    numbers9x4.clear()
    numbers9x4 = {'1-9': [list(range(1, 10, 1))], '10-18': [list(range(10, 19, 1))], '19-27': [list(range(19, 28, 1))],
                  '28-36': [list(range(28, 37, 1))], '1-18/odd': [list(range(1, 19, 2))],
                  '1-18/even': [list(range(2, 19, 2))], '19-36/odd': [list(range(19, 37, 2))],
                  '19-36/even': [list(range(20, 37, 2))],
                  '1-18/red': [list(set(numbers18x2["1-18"][0]).intersection(set(numbers18x2["red"][0])))],
                  '1-18/black': [list(set(numbers18x2["1-18"][0]).intersection(set(numbers18x2["black"][0])))],
                  '19-36/red': [list(set(numbers18x2["19-36"][0]).intersection(set(numbers18x2["red"][0])))],
                  '19-36/black': [list(set(numbers18x2["19-36"][0]).intersection(set(numbers18x2["black"][0])))],
                  'odd/red': [list(set(numbers18x2["odd"][0]).intersection(set(numbers18x2["red"][0])))],
                  'odd/black': [list(set(numbers18x2["odd"][0]).intersection(set(numbers18x2["black"][0])))],
                  'even/red': [list(set(numbers18x2["even"][0]).intersection(set(numbers18x2["red"][0])))],
                  'even/black': [list(set(numbers18x2["even"][0]).intersection(set(numbers18x2["black"][0])))]}
    for key in numbers9x4.keys():
        numbers9x4[key].extend([[], [0], [0], [0]])
    for m in range(len(stats)):
        for key in numbers9x4.keys():
            if stats[m] in numbers9x4[key][0]:
                numbers9x4[key][1].append(m)
            else:
                pass

    n_group_2_3list(numbers9x4, 9)
    n_group_4list(numbers9x4)
    return numbers9x4


numbers6x6: Dict[str, list] = {}  # Речник за числата разделени на шест "6-ци"


def numbers6x6_def() -> object:
    global numbers6x6, stats
    numbers6x6.clear()
    numbers6x6 = {'1-6': [list(range(1, 7, 1))], '7-12': [list(range(7, 13, 1))],
                  '13-18': [list(range(13, 19, 1))], '19-24': [list(range(19, 25, 1))],
                  '25-30': [list(range(25, 31, 1))], '31-36': [list(range(31, 37, 1))],
                  '1/16': [list(range(1, 17, 3))], '2/17': [list(range(2, 18, 3))],
                  '3/18': [list(range(3, 19, 3))], '19/34': [list(range(19, 35, 3))],
                  '20/35': [list(range(20, 36, 3))], '21/36': [list(range(21, 37, 3))],
                  '1-12/odd': [list(range(1, 13, 2))], '1-12/even': [list(range(2, 13, 2))],
                  '13-24/odd': [list(range(13, 25, 2))], '13-24/even': [list(range(14, 25, 2))],
                  '25-36/odd': [list(range(25, 37, 2))], '25-36/even': [list(range(26, 37, 2))],
                  '1-12/red': [[1, 3, 5, 7, 9, 12]], '1-12/black': [[2, 4, 6, 8, 10, 11]],
                  '13-24/red': [[14, 16, 18, 19, 21, 23]], '13-24/black': [[13, 15, 17, 20, 22, 24]],
                  '25-36/red': [[25, 27, 30, 32, 34, 36]], '25-36/black': [[26, 28, 29, 31, 33, 35]],
                  '1/34-odd': [list(range(1, 37, 6))], '1/34-even': [list(range(4, 37, 6))],
                  '2/35-odd': [list(range(5, 37, 6))], '2/35-even': [list(range(2, 37, 6))],
                  '3/36-odd': [list(range(3, 37, 6))], '3/36-even': [list(range(6, 37, 6))],
                  '1/34-red': [[1, 7, 16, 19, 25, 34]], '1/34-black': [[4, 10, 13, 22, 28, 31]],
                  '2/35-red': [[5, 14, 23, 32]], '2/35-black': [[2, 8, 11, 17, 20, 26, 29, 35]],
                  '3/36-red': [[3, 9, 12, 18, 21, 27, 30, 36]], '3/36-black': [[6, 15, 24, 33]]}
    for key in numbers6x6.keys():
        numbers6x6[key].extend([[], [0], [0], [0]])
    for m in range(len(stats)):
        for key in numbers6x6.keys():
            if stats[m] in numbers6x6[key][0]:
                numbers6x6[key][1].append(m)
            else:
                pass

    n_group_2_3list(numbers6x6, 6)
    for key in numbers6x6:  # Записва във вторият лист на втора позиция разликата от нормалното разпределение в
        # проценти
        if len(stats) > 0:
            if key == '2/35-red' or key == '3/36-black':
                numbers6x6[key][2][1] = (round(((numbers6x6[key][2][0]) * 37 * 100 / (4 * len(stats)) - 100), 2))
            elif key == '2/35-black' or key == '3/36-red':
                numbers6x6[key][2][1] = (round(((numbers6x6[key][2][0]) * 37 * 100 / (8 * len(stats)) - 100), 2))
            else:
                pass
    n_group_4list(numbers6x6)
    return numbers6x6


numbers3x12: Dict[tuple, list] = {}  # Речник за числата разделени на дванадесет "3-ки"


def numbers3x12_def() -> object:
    global numbers3x12, stats
    numbers3x12.clear()
    numbers3x12 = {(1, 2, 3): [], (4, 5, 6): [], (7, 8, 9): [], (10, 11, 12): [], (13, 14, 15): [], (16, 17, 18): [],
                   (19, 20, 21): [], (22, 23, 24): [], (25, 26, 27): [], (28, 29, 30): [], (31, 32, 33): [],
                   (34, 35, 36): [], (1, 4, 7): [], (2, 5, 8): [], (3, 6, 9): [], (10, 13, 16): [], (11, 14, 17): [],
                   (12, 15, 18): [], (19, 22, 25): [], (20, 23, 26): [], (21, 24, 27): [], (28, 31, 34): [],
                   (29, 32, 35): [], (30, 33, 36): [], (1, 3, 5): [], (2, 4, 6): [], (7, 9, 11): [], (8, 10, 12): [],
                   (13, 15, 17): [], (14, 16, 18): [], (19, 21, 23): [], (20, 22, 24): [], (25, 27, 29): [],
                   (26, 28, 30): [], (31, 33, 35): [], (32, 34, 36): [], (1, 7, 13): [], (4, 10, 16): [],
                   (5, 11, 17): [], (2, 8, 14): [], (3, 9, 15): [], (6, 12, 18): [], (19, 25, 31): [], (22, 28, 34): [],
                   (23, 29, 35): [], (20, 26, 32): [], (21, 27, 33): [], (24, 30, 36): []}
    for key in numbers3x12.keys():
        numbers3x12[key] = [list(key)]
        numbers3x12[key].extend([[], [0], [0], [0]])
    for q in range(len(stats)):
        for key in numbers3x12.keys():
            if stats[q] in key:
                numbers3x12[key][1].append(q)
            else:
                pass
    n_group_2_3list(numbers3x12, 3)
    n_group_4list(numbers3x12)
    return numbers3x12


numbers2x18: Dict[str, list] = {}  # Речник за числата разделени на 18 "2-ки"


def numbers2x18_def() -> object:
    global numbers2x18, stats
    numbers2x18.clear()
    numbers2x18 = {(1, 4): [], (2, 5): [], (3, 6): [], (7, 10): [], (8, 11): [], (9, 12): [], (13, 16): [],
                   (14, 17): [], (15, 18): [], (19, 22): [], (20, 23): [], (21, 24): [], (25, 28): [], (26, 29): [],
                   (27, 30): [], (31, 34): [], (32, 35): [], (33, 36): [], (1, 7): [], (2, 8): [], (3, 9): [],
                   (4, 10): [], (5, 11): [], (6, 12): [], (13, 19): [], (14, 20): [], (15, 21): [], (16, 22): [],
                   (17, 23): [], (18, 24): [], (25, 31): [], (26, 32): [], (27, 33): [], (28, 34): [], (29, 35): [],
                   (30, 36): []}
    for key in numbers2x18.keys():
        numbers2x18[key] = [list(key)]
        numbers2x18[key].extend([[], [0], [0], [0]])
    for q in range(len(stats)):
        for key in numbers2x18.keys():
            if stats[q] in key:
                numbers2x18[key][1].append(q)
    n_group_2_3list(numbers2x18, 2)
    n_group_4list(numbers2x18)
    return numbers2x18


def color_labels(numb: int, ind: int) -> object:  # Оцветява числата в етикетите от статистиката
    global labels
    if numb in red_numbers:
        labels[ind].config(fg="red", bg="white")
    elif numb in black_numbers:
        labels[ind].config(fg="black", bg="white")
    else:
        labels[ind].config(fg="green", bg="white")
    return labels[ind]


def labels_def():  # Етикетите на последните 20 числа от статистиката
    global stats, labels
    for p in labels:
        p.destroy()
    labels.clear()
    if len(stats) > 20:
        for q in range(20):
            labels.append(
                Label(roulette, text=str(stats[len(stats) - 20 + q]), font=("Times New Roman", 14, "bold"),
                      borderwidth=2, relief="sunken"))
            labels[len(labels) - 1].place(relwidth=0.12, relheight=0.04, relx=0.88, rely=0.04 * (19 - q), x=- 3,
                                          y=3)
            color_labels((stats[len(stats) - 20 + q]), (len(labels) - 1))
    elif 0 < len(stats) <= 20:
        for q in range(len(stats)):
            labels.append(Label(roulette, text=str(stats[q]), font=("Times New Roman", 14, "bold"), borderwidth=2,
                                relief="sunken", width=2))
            labels[len(labels) - 1].place(relwidth=0.12, relheight=0.04, relx=0.88,
                                          rely=0.04 * (len(stats) - 1 - q),
                                          x=0, y=2)
            color_labels(stats[q], len(labels) - 1)


def read_file():  # Чете файлът със статистиката и ги записва в списък
    global lines, stats
    with open('Roulette Statistic.txt', "r") as file_stat:
        lines = file_stat.readlines()  # Чете файлът и записва като символи числата в списък
    file_stat.close()
    stats = list(map(int, lines))  # Превръща символите в числа и ги записва в списък
    statistic_update()
    labels_def()
    # return lines, stats


def statistic_update():
    global stats, counts, numbers37, numbers12x3, numbers4x9, numbers18x2, numbers9x4
    for n in range(37):
        counts[0][n] = n  # Числата от 0 до 36 на първа позиция в листът
        counts[1][n] = stats.count(n)  # Колко пъти се среща всяко число в статистиката на втора позиция в листът

    numbers37_def()
    numbers12x3_def()
    numbers4x9_def()
    numbers18x2_def()
    numbers9x4_def()
    numbers6x6_def()
    numbers3x12_def()
    numbers2x18_def()

    # print(numbers4x9.items())
    # print(lines)
    print(numbers37)
    print(numbers12x3)
    print(numbers4x9)
    print(numbers18x2)
    print(numbers9x4)
    print(numbers6x6)
    print(numbers3x12)
    print(numbers2x18)
    print(math.comb(1, 0))
    print(pow(37, 2))

    # print(tuple(filter(lambda x: (x != 0), numbers6x6['1-6'][3])))
    # labels_def()
    # print(counts)
    # return stats, counts, numbers37, numbers12x3, numbers4x9


def labels_num_def():  # Етикетите с процентите на всяко число от 0 до 36
    global labels_num, numbers37, red_numbers, black_numbers
    for p in range(37):
        if len(labels_num) < 37:
            labels_num.append(Label(roulette, text="%", font=("Arial", 8), borderwidth=1, relief="sunken"))
            if p in range(1, 37, 3):
                labels_num[p].place(relwidth=0.19, relheight=0.03, relx=0.28, rely=0.03 + (p - 1) / 3 * 0.03)
            elif p in range(2, 37, 3):
                labels_num[p].place(relwidth=0.19, relheight=0.03, relx=0.28 + 0.19, rely=0.03 + (p - 2) / 3 * 0.03)
            elif p in range(3, 37, 3):
                labels_num[p].place(relwidth=0.19, relheight=0.03, relx=0.28 + 0.19 * 2,
                                    rely=0.03 + (p - 3) / 3 * 0.03)
            else:
                labels_num[p].place(relwidth=0.19, relheight=0.03, relx=0.28, rely=0)
            if p in red_numbers:
                labels_num[p].config(bg="#F3758C")
            elif p in black_numbers:
                labels_num[p].config(bg="#3E4B61", fg="white")
            else:
                labels_num[0].config(bg="#A2EF77")
        else:
            if numbers37[p][2][1] > 0:
                labels_num[p].config(text='+' + str(numbers37[p][2][1]) + '%')
            elif numbers37[p][2][1] <= 0:
                labels_num[p].config(text=str(numbers37[p][2][1]) + '%')


def labels_4x9_12x3_def() -> object:
    global labels_4x9_12x3, numbers4x9, numbers12x3
    if len(labels_4x9_12x3) < 15:
        for p in range(9):
            labels_4x9_12x3.append(Label(roulette, text="%4x9", bg="#EAD7AC", borderwidth=1, relief="sunken"))
            labels_4x9_12x3[p].place(relwidth=0.19, relheight=0.03, relx=0.28 + 0.19 * (p % 3),
                                     rely=0.424 + int(p / 3) * 0.03)
        for q in range(9, 12):
            labels_4x9_12x3.append(
                Label(roulette, text="%12x3", bg="#1250EA", fg="white", borderwidth=1, relief="ridge"))
            labels_4x9_12x3[q].place(relwidth=0.19, relheight=0.03, relx=0.28 + 0.19 * (q - 9), rely=0.394)
        for q in range(12, 15):
            labels_4x9_12x3.append(
                Label(roulette, text="%12x3", bg="#1250EA", fg="white", borderwidth=1, relief="ridge"))
            labels_4x9_12x3[q].place(relwidth=0.19, relheight=0.03, relx=0.09, rely=0.424 + 0.03 * (q - 12))
    else:
        k = 0
        for key in list(numbers4x9.keys())[0:9]:
            if numbers4x9[key][2][1] > 0:
                labels_4x9_12x3[k].config(text='+' + str(numbers4x9[key][2][1]) + '%')
                k = k + 1
            elif numbers4x9[key][2][1] <= 0:
                labels_4x9_12x3[k].config(text=str(numbers4x9[key][2][1]) + '%')
                k = k + 1
        j = 0
        for key in list(numbers12x3.keys())[0:9]:
            if numbers12x3[key][2][1] > 0:
                labels_4x9_12x3[j + 9].config(text='+' + str(numbers12x3[key][2][1]) + '%')
            elif numbers12x3[key][2][1] <= 0:
                labels_4x9_12x3[j + 9].config(text=str(numbers12x3[key][2][1]) + '%')
            j = j + 1
    return labels_4x9_12x3


def labels_18x2_def():
    global labels_18x2, numbers18x2
    if len(labels_18x2) < 6:
        for keys in range(len(numbers18x2.keys())):
            if keys % 2 == 0:
                h = ["half", "odd/even", "red/black"]
                i = int(keys / 2)
                buttons_calc.append(Button(roulette, text=f"{h[i]}", font=("Arial", 8, "italic")))
                buttons_calc[int(keys / 2)].place(relwidth=0.19, relheight=0.03, relx=0.28,
                                                  rely=0.514 + 0.03 * int(keys) / 2)
            labels_18x2.append(
                Label(roulette, text=str(list(numbers18x2.keys())[keys]), font=("Arial", 8), bg="brown",
                      fg="white", borderwidth=1, relief="ridge"))
            labels_18x2[keys].place(relwidth=0.19, relheight=0.03, relx=0.47 + 0.19 * (int(keys) % 2 != 0),
                                    rely=0.514 + 0.03 * int(round(keys) / 2))
    else:
        k = 0
        for key in list(numbers18x2.keys()):
            if numbers18x2[key][2][1] > 0:
                labels_18x2[k].config(text='+' + str(numbers18x2[key][2][1]) + '%')
                k = k + 1
            elif numbers18x2[key][2][1] <= 0:
                labels_18x2[k].config(text=str(numbers18x2[key][2][1]) + '%')
                k = k + 1


def button_num(n):
    global stats, lines
    stats.append(n)
    lines.append(str(n))

    with open('Roulette Statistic.txt', 'a') as file_stat:
        fileline = os.stat('Roulette Statistic.txt').st_size  # Проверява големината на файлът
        if fileline != 0:  # Ако файлът не е празен
            file_stat.seek(0, 2)  # Отива в краят на файлът
            file_stat.writelines("\n")  # Премества позицията на нов ред
            file_stat.writelines("".join(str(stats[len(stats) - 1])))
        else:
            file_stat.writelines("".join(str(n)))
    file_stat.close()

    read_file()
    buttons_mod()
    buttons[n].focus_set()

    # return lines, stats


read_file()
var_list: List[int] = [False] * 55
var: List[BooleanVar] = [BooleanVar(value=False, name=f'PY_VAR{i}') for i in range(55)]


def check_state(ind):
    global var
    if ind in range(37, 40):
        for a1 in range(12):
            buttons_bet[(a1 + 1) + (ind - 37) * 12].select()
    elif ind in range(40, 46):
        for a2 in numbers18x2[list(numbers18x2.keys())[ind - 40]][0]:
            buttons_bet[a2].select()
    elif ind in range(46, 52):
        for a3 in numbers6x6[list(numbers6x6.keys())[ind - 46]][0]:
            buttons_bet[a3].select()
    elif ind in range(52, 55):
        for a4 in numbers12x3[list(numbers12x3.keys())[57 - ind]][0]:
            buttons_bet[a4].select()
    for i in range(55):
        var_list[i] = var[i].get()
        if var[i].get():
            if i in black_numbers:
                buttons_bet[i].config(fg='black')
            elif i in red_numbers:
                buttons_bet[i].config(fg='red')
            elif i == 0:
                buttons_bet[0].config(fg='green')
            else:
                buttons_bet[i].config(fg='purple', selectcolor='yellow')
        else:
            buttons_bet[i].config(fg='white')

    print(var)
    print(var_list)


print(var_list)
for num in range(37):  # Слага бутоните на числата от рулетката и етикетите със процентите от статистиката
    # var.append(BooleanVar(value=-num - 2))
    # var.set(num)
    buttons.append(Button(roulette, text=str(num), font=("Arial", 10, "bold"), command=lambda n=num: button_num(n)))
    buttons[num].place(relwidth=0.09, relheight=0.03, relx=(0.09 * (((num % 3) + 2) % 3)) * int(num > 0),
                       rely=(0.03 + 0.03 * int((num - 1) / 3)) * int(num > 0))
    buttons_bet.append(Checkbutton(roulette, text=str(num), font=("Arial", 8, "bold"), variable=var[num], onvalue=True,
                                   offvalue=False, indicatoron=False, command=lambda a=num: check_state(a)))
    buttons_bet[num].place(relwidth=0.071, relheight=0.025 + 0.05 * int(num == 0),
                           rely=(0.945 - 0.025 * (((num % 3) + 2) % 3)),
                           relx=(0.071 + 0.071 * int((num - 1) / 3)) * int(num > 0))
    if num in red_numbers:
        buttons[num].config(bg="red", fg="white")
        buttons_bet[num].config(bg="red", fg="white")
    elif num in black_numbers:
        buttons[num].config(bg="black", fg="white")
        buttons_bet[num].config(bg="black", fg="white")
    else:
        buttons[0].config(bg="green", fg="white")
        buttons_bet[0].config(bg="green", fg="white")
    button_text.append(buttons[num].cget('text'))

for bet in range(18):
    # var.append(BooleanVar(value=-bet - 39))
    # var.set(0)
    buttons_bet.append(Checkbutton(roulette, font=("Arial", 8, "bold"), variable=var[bet + 37], onvalue=True,
                                   offvalue=False, indicatoron=False, command=lambda a=bet + 37: check_state(a)))
    # var_list[bet + 37] = [var.get()]
    # print(buttons_bet[bet + 37].cget('offvalue'))
    buttons_bet[37 + bet].place(relwidth=0.284 * int(bet < 15) / (1 + int(bet > 2)) + 0.077 * int(bet > 14),
                                relheight=0.025, relx=0.071 + bet * int(bet < 3) * 0.284 + (bet - 3) * int(
            9 > bet > 3) * 0.142 + (bet - 9) * int(15 > bet > 9) * 0.142 + 12 * 0.071 * int(bet > 14),
                                rely=0.87 - 0.025 * int(9 > bet > 2) - 0.050 * int(15 > bet > 8) + 0.025 * (
                                        bet - 14) * int(bet > 14))
    if 0 <= bet <= 2:
        buttons_bet[bet + 37].config(bg="#1250EA", fg="white", text=str(list(numbers12x3.keys())[bet]))
    elif 3 <= bet <= 8:
        buttons_bet[bet + 37].config(bg="brown", fg="white", text=str(list(numbers18x2.keys())[bet - 3]))
    elif 9 <= bet <= 14:
        buttons_bet[bet + 37].config(bg="purple", fg="white", text=str(list(numbers6x6.keys())[bet - 9]))
    else:
        buttons_bet[bet + 37].config(bg="#1250EA", fg="white", text='3:1')


def reset(a):
    if a == 0:
        for i in range(37, 40):
            if var[i].get():
                for i1 in range(12):
                    buttons_bet[(i1 + 1) + (i - 37) * 12].deselect()
                    buttons_bet[(i1 + 1) + (i - 37) * 12].config(fg='white')
                buttons_bet[i].deselect()
                buttons_bet[i].config(fg='white')
    elif a == 1:
        for j in range(40, 46):
            if var[j].get():
                for a2 in numbers18x2[list(numbers18x2.keys())[j - 40]][0]:
                    buttons_bet[a2].deselect()
                    buttons_bet[a2].config(fg='white')
            buttons_bet[j].deselect()
            buttons_bet[j].config(fg='white')
    elif a == 2:
        for k in range(46, 52):
            if var[k].get():
                for a3 in numbers6x6[list(numbers6x6.keys())[k - 46]][0]:
                    buttons_bet[a3].deselect()
                    buttons_bet[a3].config(fg='white')
            buttons_bet[k].deselect()
            buttons_bet[k].config(fg='white')
    elif a == 3:
        for m in range(52, 55):
            if var[m].get():
                for a4 in numbers12x3[list(numbers12x3.keys())[57 - m]][0]:
                    buttons_bet[a4].deselect()
                    buttons_bet[a4].config(fg='white')
            buttons_bet[m].deselect()
            buttons_bet[m].config(fg='white')
    else:
        for n in range(55):
            buttons_bet[n].deselect()
            buttons_bet[n].config(fg='white')


for res in range(5):
    buttons_reset.append(Button(roulette, text="C", font=("Arial", 9, "bold"), justify=LEFT, bg="pink", fg="black",
                                command=lambda n=res: reset(n)))
    buttons_reset[res].place(relwidth=0.071 + 0.006 * int(res >= 3), relheight=0.025, relx=0 + int(res >= 3) * 0.923,
                             rely=0.87 - 0.025 * res * int(res < 3) - 0.025 * (res - 3) * int(res > 3))
labels_num_def()
labels_4x9_12x3_def()
labels_18x2_def()


def roll_roulette():
    global lines, labels, stats
    n = roll_num.get()
    try:
        n = int(n)
    except ValueError:
        n = 1
    while n > 0:
        rnd = randint(0, 36)
        with open('Roulette Statistic.txt', 'a') as file_stat:
            if len(lines) != 0:  # Ако файлът не е празен
                file_stat.seek(0, 2)  # Отива в краят на файлът
                file_stat.writelines("\n")  # Премества позицията на нов ред
                file_stat.writelines("".join(str(rnd)))
            else:
                fileline = os.stat('Roulette Statistic.txt').st_size  # Проверява големината на файлът
                if fileline != 0:  # Ако файлът не е празен
                    file_stat.seek(0, 2)  # Отива в краят на файлът
                    file_stat.writelines("\n")  # Премества позицията на нов ред
                    file_stat.writelines("".join(str(rnd)))
                else:
                    file_stat.writelines(str(rnd))
                # print(rnd)
        file_stat.close()
        n = n - 1
    read_file()
    buttons_mod()
    button_random.focus_set()


def clear_stat():  # Изтрива статистиката
    global lines, stats

    with open('Roulette Statistic.txt', 'w') as file_stat:
        file_stat.writelines("")
    file_stat.close()
    read_file()
    buttons_mod()
    button_clear.focus_set()
    # return lines, stats


def half_stat():  # Изтрива първата половина от статистиката
    global lines, stats

    if len(stats) == 1:  # Ако в статистиката има само едно число
        lines.clear()  # Изтрива всичко от спискът със символите от статистиката
        stats.clear()  # Изтрива числото от статистиката
        with open('Roulette Statistic.txt', 'w') as file_stat:
            file_stat.write("")
        file_stat.close()
    elif len(stats) > 1:
        half = int(len(lines) / 2)
        del lines[0:half]  # Изтрива първата половина от символите в статистиката
        del stats[0:half]  # Изтрива първата половина от числата в статистиката
        with open('Roulette Statistic.txt', 'w') as file_stat:
            file_stat.write("")
        file_stat.close()
        with open('Roulette Statistic.txt', 'a') as file_stat:
            for p in range(len(lines)):
                if p != 0:  # Ако файлът не е празен
                    file_stat.seek(0, 2)  # Отива в краят на файлът
                    file_stat.writelines("\n")  # Премества позицията на нов ред
                    file_stat.writelines("".join(str(stats[p])))
                elif p == 0 and len(lines) != 0:
                    file_stat.writelines("".join(str(stats[0])))
        file_stat.close()

    read_file()
    buttons_mod()
    # return lines, stats


def undo():  # Премахва последното число от статистиката
    global lines, stats
    n = undo_num.get()
    try:
        n = int(n)
    except ValueError:
        n = 1
    if 0 < len(stats) - n <= 10:
        del lines[len(lines) - n:]
        del stats[len(stats) - n:]
    elif len(stats) - n > 10:
        del lines[len(lines) - n:]
        del stats[len(stats) - n:]
    else:
        lines.clear()
        stats.clear()
    with open('Roulette Statistic.txt', 'w') as file_stat:
        for p in range(len(lines)):  #
            if p != 0:  # Ако файлът не е празен
                file_stat.seek(0, 2)  # Отива в краят на файлът
                file_stat.writelines("\n")  # Премества позицията на нов ред
                file_stat.writelines("".join(str(stats[p])))
            elif p == 0 and len(lines) != 0:
                file_stat.writelines("".join(str(stats[0])))
    file_stat.close()
    read_file()
    buttons_mod()
    button_undo.focus_set()
    return lines, stats

    # num_roll = 3


def buttons_mod():
    roll_num.focus_set()
    roll_num.config(insertontime=0)
    undo_num.focus_set()
    undo_num.config(insertontime=0)
    button_clear.config(text="Clear Stat (" + str(len(stats)) + ")")
    button_half.config(text="Half Stat (" + str(int(len(stats) / 2)) + ")")


separator1: Separator = ttk.Separator(roulette, orient='vertical')
separator1.place(relx=0.28, rely=0, relwidth=0, relheight=0.75)
separator2: Separator = ttk.Separator(roulette, orient='vertical')
separator2.place(relx=0.850, rely=0, relwidth=0, relheight=0.75)
separator3: Separator = ttk.Separator(roulette, orient='horizontal')
separator3.place(relx=0, rely=0.392, relwidth=0.865, relheight=0)
roll_num: Entry = Entry(roulette, relief="sunken", cursor="dot", insertofftime=0, insertwidth=1, justify=CENTER,
                        font=("Arial", 10, "italic"), state=NORMAL)
roll_num.place(relwidth=0.09, relheight=0.03, relx=0.18, rely=0)
undo_num: Entry = Entry(roulette, relief="sunken", cursor="dot", insertofftime=0, insertwidth=1, justify=CENTER,
                        font=("Arial", 10, "bold"), state=NORMAL)
undo_num.place(relwidth=0.135, relheight=0.03, relx=0.135, rely=0.97)
button_random: Button = Button(roulette, text="Roll", font=("Arial", 9), justify=LEFT, bg="yellow",
                               command=lambda: roll_roulette())
button_random.place(relwidth=0.09, relheight=0.03, relx=0.09, rely=0)
button_clear: Button = Button(roulette, text="Clear Stat (" + str(len(stats)) + ")", font=("Arial", 8),
                              command=lambda: clear_stat())
button_clear.place(relwidth=0.270, relheight=0.03, relx=0.540, rely=0.97)
button_half: Button = Button(roulette, text="Half Stat (" + str(int(len(stats) / 2)) + ")", font=("Arial", 8),
                             command=lambda: half_stat())
button_half.place(relwidth=0.270, relheight=0.03, relx=0.270, rely=0.97)
button_undo: Button = Button(roulette, text='Undo', font=("Arial", 10), command=lambda: undo())
button_undo.place(relwidth=0.135, relheight=0.03, relx=0, rely=0.97)
button_stat: Button = Button(roulette, text="%", font=("Arial", 10), command=lambda: labels_num_def())
button_stat.place(relwidth=0.135, relheight=0.03, relx=0.47, rely=0)
button_4x9_12x3: Button = Button(roulette, text="Calc", font=("Arial", 10), bg='#CA60E2',
                                 command=lambda: [labels_num_def(), labels_4x9_12x3_def(), labels_18x2_def()])
button_4x9_12x3.place(relwidth=0.19, relheight=0.03, relx=0.09, rely=0.394)
button_calc: Button = Button(roulette, text="%", font=("Arial", 8), bg='#EAD271',
                             command=lambda: labels_4x9_12x3_def())
button_calc.place(relwidth=0.09, relheight=0.03, relx=0, rely=0.394)
# roll_roulette(roll_num.get())

# print(lines)
# print(stats)
roulette.attributes('-topmost', True)
roulette.mainloop()
