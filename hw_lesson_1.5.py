class Animals():
    """Common class of animals"""

    def __init__(self, name: str, food: str, weight: float, voice: str):
        self.name = name
        self.food = food
        self.weight = weight
        self.voice = voice

    def feed(self):
        print('Thank you for feeding me with the {}.'.format(self.food))

    def identify_itself(self):
        print('My name is {}'.format(self.name))
        print('I eat {}.'.format(self.food))
        print('My weight {}kg.'.format(self.weight))
        print('I say {}'.format(self.voice))

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_voice(self):
        return self.voice


class Birds(Animals):
    """Class of birds"""

    def __init__(self, name: str, food: str, weight: float, voice: str, num_eggs: int):
        super().__init__(name, food, weight, voice)
        self.num_eggs = num_eggs

    def get_egg(self):
        self.num_eggs -= 1
        return 1

    def get_all_eggs(self):
        num_eggs = self.num_eggs
        self.num_eggs = 0
        return num_eggs


class Artiodactyls(Animals):
    """Class of Artodactils"""

    pass

class Wool(Artiodactyls):
    """Class of wool"""

    def __init__(self, name: str, food: str, weight: float, voice: str, num_wool: int):
        super().__init__(name, food, weight, voice)
        self.num_wool = num_wool

    def get_wool(self):
        num_milk = self.num_wool
        self.num_milk = 0
        return num_milk


class Dairy(Artiodactyls):
    """Class of Dairy"""

    def __init__(self, name: str, food: str, weight: float, voice: str, num_milk: int):
        super().__init__(name, food, weight, voice)
        self.num_milk = num_milk

    def get_half_milk(self):
        self.num_milk /= 2
        return self.num_milk

    def get_all_milk(self):
        num_milk = self.num_milk
        self.num_milk = 0
        return num_milk


if __name__ == '__main__':
    white_goose = Birds('Белый', 'Grain', 2.5, 'Ga-ga', 4)
    gray_goose = Birds('Серый', 'Grain', 3.3, 'Ga-ga', 7)
    cow = Dairy('Манька', 'Hay', 551, 'Mu-mu', 21)
    sheep_aries = Wool('Барашек', 'Hay', 120, 'Be-be', 6)
    sheep_curly = Wool('Кудрявый', 'Hay', 100, 'Be-be', 7)
    hen_ko = Birds('Ko-ko', 'Grain', 2.5, 'Ko-ko', 170)
    hen_ku = Birds('Кукареку', 'Grain', 4.5, 'Ko-ko', 190)
    goat_horn = Dairy('Рога', 'Hay', 90, 'Me-me', 7)
    goat_hoof = Dairy('Копыта', 'Hay', 112, 'Me-me', 10)
    duck = Birds('Кряква', 'Grain', 1.6, 'Krya-kray', 13)

    print(white_goose.get_name().center(10, '='))
    white_goose.feed()
    print(white_goose.get_egg())
    print(white_goose.get_all_eggs())

    print(gray_goose.get_name().center(10, '='))
    gray_goose.feed()
    print(gray_goose.get_egg())
    print(gray_goose.get_all_eggs())

    print(cow.get_name().center(10, '='))
    cow.feed()
    print(cow.get_half_milk())
    print(cow.get_all_milk())

    print(sheep_aries.get_name().center(10, '='))
    sheep_aries.feed()
    print(sheep_aries.get_wool())

    print(sheep_curly.get_name().center(10, '='))
    sheep_curly.feed()
    print(sheep_curly.get_wool())

    print(goat_horn.get_name().center(10, '='))
    goat_horn.feed()
    print(goat_horn.get_half_milk())
    print(goat_horn.get_all_milk())

    print(goat_hoof.get_name().center(10, '='))
    goat_hoof.feed()
    print(goat_hoof.get_half_milk())
    print(goat_hoof.get_all_milk())

    print(duck.get_name().center(10, '='))
    duck.feed()
    print(duck.get_egg())
    print(duck.get_all_eggs())

    tuple_animals = (
        white_goose,
        gray_goose,
        cow,
        sheep_aries,
        sheep_curly,
        hen_ko,
        hen_ku,
        goat_horn,
        goat_hoof,
        duck
    )

    anim_max_weight = {'Name': None, 'Weight': 0}
    total_weight = 0
    for inst_anim in tuple_animals:
        total_weight += inst_anim.get_weight()
        if anim_max_weight['Weight'] < inst_anim.get_weight():
            anim_max_weight.update({'Name': inst_anim.get_name(), 'Weight': inst_anim.get_weight()})

    print('Total weight: {}kg.'.format(total_weight))
    print('Maximum weight : {}kg. Name of animal: {}'.format(anim_max_weight['Weight'], anim_max_weight['Name']))
