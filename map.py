from wine import Wine

class Map:
    all_regions:dict[str:dict[str:Wine]] = {} #{country:{region_1:[wine_1_1, wine_1_2]...}}

    def __init__(self, user, img='', color = 'white') -> None:
        self.user = user
        self.unlocked_regions:dict[str:dict[str:Wine]] = {} #{country:{region_1:[wine_1_1, wine_1_2]...}}
        self.background = color
        self.image = img


    def add_wine_to_the_map(self, wine:'Wine'):
        self.all_regions[wine.country][wine.region] = wine
