import random
file = open("stat_sheet.txt", "r+")

stats = {
    "str": 0,
    "dex": 0,
    "con": 0,
    "wis": 0,
    "int": 0,
    "cha": 0,
}


stat_sheet = file.read()
stat_sheet = stat_sheet.split("\n")
print(stat_sheet)

for s in stats:
    stats[s] = stat_sheet.pop(0)
print(stat_sheet)

print(stats)


def stat_roll():
    x, y, z, w = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
    num = [x, y, z, w]
    num.sort()
    num.pop(0)
    total = 0
    for a in num:
        total += a
    return total


def stat_setter(a):
    while a not in raw_nums:
        x = input(f"What do you want to assign to {s}?\n")
        try:
            x = int(x)
            if x not in raw_nums:
                print("That's not an option!")
            else:
                a = x
        except:
            print("That's not an option!")
    return a


blank_stat = 0


# st, d, c, w, i, c = stat_roll(), stat_roll(), stat_roll(), stat_roll(), stat_roll(), stat_roll()
# raw_nums = [st, d, c, w, i, c]
# empty = []
# print(f'{st}, {d}, {c}, {w}, {i}, and {c} are your stats')
#
# for s in stats:
#     stats[s] = stat_setter(blank_stat)
#     raw_nums.remove(stats[s])
#     if raw_nums != empty:
#         print(raw_nums)
#
#
# for s, z in stats.items():
#     file.write(f'{s}:{z}\n')
# print(stats)
