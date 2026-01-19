#Uppgift 2b
fullpris = 2000
egen_rea = int(input('Hur många procent rea är det på jackan?\n'))

jacka_rea = fullpris * (egen_rea / 100)
print(f'Jackan kostar {jacka_rea}kr')
#print('Jackan kostar ' + str(jacka_rea)+'kr')