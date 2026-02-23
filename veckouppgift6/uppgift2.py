class Country:

    def __init__(self, name, pop, area=None):            # Arean sätts som standard till None om inget anges
        self.name = name
        self.pop = pop
        self.area = area
        self.languages = []

    def print_info(self):
        landinfo = f'I {self.name} bor det {self.pop} miljoner invånare'
        if self.area != None:
            landinfo += f'och arean är {self.area}'      # Lägger till arean på textsträngen om arean inte är None
        print(landinfo)
        if self.languages != None:                       # Om listan inte är tom, skriv ut landets språk
            print('Språk för landet:')
            for item in self.languages:                  # Loopa igenom listan och skriv ut varje språk på egen rad
                print(f'{item}')

    def add_language(self, language):
        self.languages.append(language)                  # Append lägger till nya språket sist i listan self.languages


se = Country("Sverige", 10.5, 450295)     # Skapar objekt av klassen country
se.add_language("Svenska")                               # Anropar add_language metoden för att lägga till språket i listan
no = Country("Norge", 5.5, 385207)
no.add_language('Norska')
dk = Country('Danmark', 6.0, 42952)
fin = Country('Finland', 3.8, 103000)
fin.add_language('Svenska')                              # Lägger till språken för Finland på två rader för metoden är byggd för att ta emot ett språk i taget
fin.add_language('Finska')
dk.print_info()                                          # Här körs metoden
fin.print_info()