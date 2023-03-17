"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unqi_species = set()

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        species = line.rstrip().split("|")[1]
        unqi_species.add(species)

    return unqi_species
#print(all_species('villagers.csv'))
#hello


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        name, species = line.split("|")[:2]
        if search_string in ("All",species):
            villagers.append(name)

    return sorted(villagers)
# print(get_villagers_by_species('villagers.csv', search_string="Anteater"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    data = open(filename)

    for line in data:
        villager_record = line.rstrip().split("|")

        name = villager_record[0]
        hobby = villager_record[3]

        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    sorted_hobbies = [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]

    for hobby in sorted_hobbies:
        print(hobby)
# print(all_names_by_hobby('villagers.csv'))



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    data = open(filename)

    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))

    return all_data
#print(all_data('villagers.csv'))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    for name, _, _, _, saying in all_data(filename):
        if name == villager_name:
            return saying
#print(find_motto('villagers.csv', 'Frita'))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code

    villagers = all_data(filename)

    target_personality = []

    for villager_data in villagers:

        if  villager_data[0] == villager_name:
            target_personality.append(villager_data[2])

    if target_personality:
        likeminded = set()
        for villager_data in villagers:
            if  villager_data[2] == target_personality[0]:
                likeminded.add(villager_data[0])
    
    else:
        likeminded = set()

    return likeminded
# print(find_likeminded_villagers('villagers.csv', 'Wendy'))