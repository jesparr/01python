summa = 0
antal = int(input('Hur många är ni i sällskapet? '))
dricks = input('Hur mycket dricks vill ni ge?: ')

if dricks == '':
    dricks_belopp = 10
else:
    dricks_belopp = int(dricks)

while True:
    svar = (input('Skriv in ett belopp: '))
    if svar == 'quit':
        break

    belopp = int(svar)
    summa += belopp

summa_med_dricks = summa * (1 * dricks_belopp / 100)
total_summa = summa_med_dricks + summa

print(f'Det blir {total_summa} totalt med dricks')