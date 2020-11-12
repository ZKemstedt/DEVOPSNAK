import csv
import random
from operator import itemgetter, concat
from itertools import groupby, islice
import functools

with open("lesson_9/data.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    choices = list(reader)
    random.shuffle(choices)
    print(" -------- shuffle and sort ----------")
    sorted_list = sorted(choices, key=itemgetter(1))
    print("\n".join(map(str, sorted_list)))

    winners_1_round = []
    to_place = {"Chat": 8, "Filserver": 6, "Kundregister": 6,
                "Serverhallen": 6, "Smarta Hem": 6, "Kalender": 6, "NULL": 0, "Egen uppgift": 0}

    for key, group in groupby(sorted_list, itemgetter(1)):
        winners_1_round.append([key, list(map(itemgetter(0), islice(group, to_place[key])))])

    winners = list(functools.reduce(concat, map(itemgetter(1), winners_1_round)))
    todo_sorted = list(filter(lambda x: x[0] not in winners, sorted_list))

    to_place = {**to_place, **dict(map(lambda x: (x[0], to_place[x[0]] - len(x[1])), winners_1_round))}
    winners_2_round = []
    for key, group in groupby(todo_sorted, itemgetter(2)):
        winners_2_round.append([key, list(map(itemgetter(0), islice(group, to_place[key])))])

    winners_2 = list(functools.reduce(concat, map(itemgetter(1), winners_2_round)))
    todo_sorted_2 = list(filter(lambda x: x[0] not in winners_2, todo_sorted))

    to_place = {**to_place, **dict(map(lambda x: (x[0], to_place[x[0]] - len(x[1])), winners_2_round))}
    winners_3_round = []
    for key, group in groupby(todo_sorted_2, itemgetter(3)):
        winners_3_round.append([key, list(map(itemgetter(0), islice(group, to_place[key])))])

    winners_3 = list(functools.reduce(concat, map(itemgetter(1), winners_3_round)))
    not_placed = list(filter(lambda x: x[0] not in winners_3, todo_sorted_2))

    print("----- result ------")
    result = []
    for row in winners_1_round:
        for person in row[1]:
            result.append((row[0], person))
    for row in winners_2_round:
        for person in row[1]:
            result.append((row[0], person))
    for row in winners_3_round:
        for person in row[1]:
            result.append((row[0], person))

    print("\n".join(map(str, sorted(result))))

    print("----- not placed ------ ")
    for row in not_placed:
        print(f"{row[0]} wish: {row[1:]}")
