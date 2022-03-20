import random
file = open("stat_sheet.txt", "r+")

player_info = {
    "stats": {
        "str": 0,
        "dex": 0,
        "con": 0,
        "wis": 0,
        "int": 0,
        "cha": 0,
    },
    "stat_ability": {
        "str_ability": 0,
        "dex_ability": 0,
        "con_ability": 0,
        "wis_ability": 0,
        "int_ability": 0,
        "cha_ability": 0,
    }
}


def ability_modifier_maker():  # takes the numbers from stats and transforms them into what they'll be for ability modifiers
    keys = list(player_info["stat_ability"].keys())
    values = list(player_info["stats"].values())
    for v in range(len(values)):
        values[v] = (values[v] - 10) // 2
    for r in range(len(player_info["stat_ability"])):
        player_info["stat_ability"][keys[r]] = values[r]


def d20():
    d20_roll = random.randint(1, 20)
    if d20_roll == 1:
        print("Critical fail!")
        return d20_roll
    elif d20_roll == 20:
        print("Critical success!")
        return d20_roll
    else:
        return d20_roll


def stat_saver():
    save = open("stat_sheet.txt", "w")
    nl = "\n"
    stat_items = list(player_info["stats"].items())
    for number in range(len(player_info["stats"])):
        key, value = stat_items[number]
        if number == len(player_info["stats"]) - 1:
            nl = ""
        save.write(f'{key}:{value}{nl}')
    save.close()


def stat_roll():
    dice1, dice2, dice3, dice4 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
    num = [dice1, dice2, dice3, dice4]
    num.sort()
    num.pop(0)
    total = 0
    for a in num:
        total += a
    return total


def stat_setter(a):
    while a not in raw_nums:
        x_temp = input(f"What do you want to assign to {s}?\n")
        try:
            x_temp = int(x_temp)
            if x_temp not in raw_nums:
                print("That's not an option!")
            else:
                a = x_temp
        except ValueError:
            print("That's not an option!")
    return a


# loads the stats back into the dictionary
stat_sheet = file.read()
if stat_sheet:
    stat_sheet = stat_sheet.split("\n")
    stat_shot = []

    for j in stat_sheet:
        stat_shot.append(j[4:])
    stat_sheet = stat_shot
    for s in player_info["stats"]:
        player_info["stats"][s] = int(stat_sheet.pop(0))
file.close()
file = open("stat_sheet.txt", "r+")

# if you already have a file on hand this will let you decide if you want to continue or restart
file_check = file.read()
file_answer = "0"
answer_options = ["yes", "no"]
if file_check:
    print(f'Do you want to load your old save with stats:\n{player_info["stats"]} \nYes/No')
    while file_answer not in answer_options:
        x = input()
        if str.lower(x) in answer_options:
            file_answer = str.lower(x)
        else:
            print("please enter \'yes\' or \'no\'")
file.close()

# this is the program that rolls the stats and uses them for a fresh build

if file_answer != "yes":
    blank_stat = 0
    st, d, c, w, i, ch = stat_roll(), stat_roll(), stat_roll(), stat_roll(), stat_roll(), stat_roll()
    raw_nums = [st, d, c, w, i, ch]
    empty = []
    print(f'{st}, {d}, {c}, {w}, {i}, and {ch} are your stats')

    for s in player_info["stats"]:
        player_info["stats"][s] = stat_setter(blank_stat)
        raw_nums.remove(player_info["stats"][s])
        if raw_nums != empty:
            print(raw_nums)

#  this turns the stats' dictionary into a usable txt folder
ability_modifier_maker()

stat_saver()
print(player_info["stats"])
print(player_info["stat_ability"])
