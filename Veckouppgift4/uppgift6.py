def increase(x):
    x += 1                      #Bytte plats på rad 4 och 5, den ökar x med 1 innan den returnerar värdet, annars hinner inte "x +=1" hända innan funktionen avslutas
    return x


print(increase(5))
