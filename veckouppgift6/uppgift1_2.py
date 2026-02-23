class Animal:                                       # Basklass
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")  # Standard-implementation som subklasser kan ärva eller skriva över


class Dog(Animal):                                  # Subklass – ärver från Animal
    def make_noise(self):                           # Ersätter basklassens version av metoden
        print("Voff!")


class Cat(Animal):                                  # Subklass – ärver från Animal
    def make_noise(self):
        super().make_noise()                        # Anropar basklassens metod först (Animal.make_noise)
                                                    # och lägger sedan till extra beteende, dvs Detta djur har...+ Mjau!
        print("Mjau!")


class Eagle(Animal):                                # Subklass – ärver från Animal
    def make_noise(self):                           # Override även här
        print("Kee-kee")


def sound_off(animal):                              # Funktion som tar emot vilket Animal-objekt som helst (Polymorfism)
    animal.make_noise()


Katten = Cat()                                      # Skapar ett object av Cat
Hunden = Dog()                                      # -||- Dog
Örnen = Eagle()                                     # -||- Eagle


sound_off(Katten)                                   # Samma funktion anropas med olika objekt
sound_off(Hunden)                                   # olika implementationer av make_noise körs (polymorfism)
sound_off(Örnen)