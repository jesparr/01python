y = 1

def femvarv(y):
    for x in range(1, 100):
        y *= 2
        if x == 5:
            return y

resultat = femvarv(y)
print(resultat)