import random

tal = random.randint(1, 100)

gissningar = 0

while True:
    gissa = int(input('Gissa på ett tal mellan 1-100\n'))
    gissningar += 1

    if gissa > tal:
        print('Nej, det är för högt!\n')
    elif gissa < tal:
        print('Nej, det är för lågt!\n')
    else:
        print(f'Du har gissat rätt, du gjorde det på {gissningar} gissningar!\n')