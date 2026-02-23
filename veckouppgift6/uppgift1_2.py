class Animal:                                       # Basklass – definierar gemensamt beteende för alla djur
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")  # Standard-implementation som subklasser kan ärva eller skriva över


class Dog(Animal):                                  # Subklass – ärver från Animal
    def make_noise(self):                           # Override: ersätter basklassens version av metoden
        print("Voff!")                              # Eget beteende för just hundar


class Cat(Animal):                                  # Subklass – ärver från Animal
    def make_noise(self):
        super().make_noise()                        # Anropar basklassens metod först (Animal.make_noise)
                                                    # och lägger sedan till extra beteende
        print("Mjau!")


class Eagle(Animal):                                # Subklass – ärver från Animal
    def make_noise(self):                           # Override även här
        print("Kee-kee")


def sound_off(animal):                              # Funktion som tar emot vilket Animal-objekt som helst
    animal.make_noise()                             # Polymorfism: rätt make_noise() körs beroende på objektets faktiska klass


Katten = Cat()                                      # Skapar ett objekt (instans) av klassen Cat
Hunden = Dog()                                      # Skapar en instans av Dog
Örnen = Eagle()                                     # Skapar en instans av Eagle


sound_off(Katten)                                   # Samma funktion anropas med olika objekt →
sound_off(Hunden)                                   # olika implementationer av make_noise() körs (polymorfism)
sound_off(Örnen)