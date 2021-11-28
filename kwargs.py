def fight_dragon(**kwargs):

    # I need to place the conditions in a dictionary?
    # or I need to get the  variables from the dictionary.

    player_hitpoints = kwargs["player_hitpoints"]
    dragon_hitpoints = kwargs["dragon_hitpoints"]
    sword = kwargs["sword"]
    dragon_asleep = kwargs["dragon_asleep"]

    if player_hitpoints > dragon_hitpoints:
        if sword:  # if sword is true
            return "Player kills dragon"
        else:
            return "Dragon eats player, you need a sword"
    if dragon_asleep and sword:
        return "player kills sleeping dragon"
    elif dragon_asleep:
        return "dragon woke up and ate the player"
    else:
        return "dragon wasn't sleeping and you didn't have a sword, you die"


game_dict = {
    "player_hitpoints": 20,
    "dragon_hitpoints": 12,
}
game_dict2 = {
    "sword": True,
    "dragon_asleep": True,
}

print(fight_dragon(**game_dict2, **game_dict))


def both(*args, **kwargs):
    pass


def normal(age, hitpoints, dragon=True):
    pass


# fight_dragon(player_hitpoints=20, dragon_hitpoints=10, sword=True, dragon_asleep=True)


# fight_dragon(game_dict)
# print(fight_dragon(20, 25, sword=True, dragon_asleep=False))


# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result


# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# my_first_dict = {"A": 1, "B": 2}
# my_second_dict = {"C": 3, "D": 4}
# my_merged_dict = {**my_first_dict, **my_second_dict}
