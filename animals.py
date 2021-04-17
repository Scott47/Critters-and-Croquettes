from datetime import date

class Llama:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.location = location
        self.walking = True

class Goat:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = ""
        self.date_added = date.today()
        self.location = location
        self.walking = True

class Ostrich:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.walking = True

class Alpaca:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.walking = True

class Elk:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.walking = True

class Cobra:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.slithering = True

class Ratsnake:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.slithering = True

class Indigo:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.slithering = True

class Brownsnake:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.slithering = True

class Copperhead:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.slithering = True

class Narwhal:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.swimming = True

class Manatee:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.swimming = True

class Whale:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.swimming = True

class Dolphin:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.swimming = True

class Shark:

    def __init__(self, location, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.location = location
        self.swimming = True

miss_fuzz = Llama('petting area', 'Drama', 'llama' )
miss_buzz = Goat('petting area', 'Billie', 'goat')
# miss_guzz = Ostrich('petting area')
# miss_cuzz = Alpaca('petting area')
# miss_huzz = Elk('petting area')
print(miss_buzz)

# miss_hiss = Cobra('glass tank')
# miss_siss = Ratsnake('glass tank')
# miss_fiss = Copperhead('glass tank')
# miss_piss = Brownsnake('glass tank')
miss_ciss = Indigo('glass tank', 'Snakey', 'reptile')
print(miss_ciss)

miss_blow = Narwhal('the pond', 'Flow', 'whale')
miss_blow.name = "mystical"
print(miss_blow)
