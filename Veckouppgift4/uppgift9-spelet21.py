from random import randint

i = 0                                       #Har bara gjort version 2

def increase(i):
    while i <= 21:                          #När i är mindre eller exakt 21,
        i += randint(1, 13)            #lägg till en random int mellan 1 och 13
        if i > 21:                          #När i är större än 21, skriv ut i
            print(i)
            return


increase(i)