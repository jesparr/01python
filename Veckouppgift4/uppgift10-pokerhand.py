import random


def spelkort():
    color = ['Ruter', 'Hjärter', 'Spader', 'Klöver']
    valor = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Knekt', 'Dam', 'Kung', 'Ess']
    random_color = random.choice(color)
    random_valor = random.choice(valor)
    kort = [random_color, random_valor]
    return kort


min_hand = spelkort()
print(min_hand)

mitt_kort1 = spelkort()
mitt_kort2 = spelkort()
if mitt_kort1 == mitt_kort2:
    print('Korten är likadana')

