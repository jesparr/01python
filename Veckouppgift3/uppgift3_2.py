summa = 0
antal = int(input('Hur många är ni i sällskapet? '))

while True:
    svar = (input('Skriv in ett belopp: '))
    if svar == 'quit':
        break
    belopp = int(svar)
    summa += belopp
    ny_summa = summa / antal
print(f'Det blir {ny_summa} totalt')