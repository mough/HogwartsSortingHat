import random


def check_for_bad_wizards(wizard):
    bad_wizards = ['draco', 'malfoy', 'salazar']
    if wizard in bad_wizards:
        return True
    else:
        return False


def check_for_clever_wizards(wizard):
    clever_wizards = ['luna', 'helena']
    if wizard in clever_wizards:
        return True
    else:
        return False


def sorting_hat(wizard):
    wizard = wizard.lower()
    if check_for_bad_wizards(wizard):
        return 'Slytherin'
    elif check_for_clever_wizards(wizard):
        return 'Ravenclaw'
    else:
        return random.choice(['Hufflepuff', 'Ravenclaw', 'Gryffindor','Slytherin'])


if __name__ == '__main__':
    print("Welcome to Hogwarts!")
    keep_sorting = True
    while keep_sorting:
        name = raw_input("\nPlease enter a first name to be sorted by the sorting hat. Enter Q to quit.")
        if name == 'Q':
            keep_sorting = False
        else:
            print "%s belongs in %s" % (name, sorting_hat(name))
    print "\nBye bye Norbert! Mommy will never forget you!"
    exit()
