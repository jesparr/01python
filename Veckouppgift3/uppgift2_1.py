#1a

answer = 0
for i in range(11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55
print('----------------------------------------------------------')

#1b

svar = 0
for i in range(101):
    svar += i
print(f'Summan av alla tal mellan 1 och 100 är {svar}')

print('----------------------------------------------------------')


#1c
loop = 0
summa = 0
while loop <= 100:
    summa += loop
    loop += 1
print(f'Summan av alla tal i loopen mellan 1 och 100 är {summa}')

