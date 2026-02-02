#Version 1
summa = 0

while True:
    svar = (input('Skriv in ett belopp: '))
    if svar == 'quit':
        break
    belopp = int(svar)
    summa += belopp
print(f'Det blir {summa} totalt')

#Version 2
