level1 = 100
level2 = 300
discount = 0


price = float(input('Välkommen, köp något dyrt: '))
final_price = price * (100 - discount) / 100

if price >= level2:
    print('Grattis! Du har avancerat till nivå 2 och får 25% rabatt.')
    discount = 25

elif price > level1:
    print('Grattis! Du har avancerat till nivå 1 och får 10% rabatt.')
    discount = discount + 10
else:
    print('Du får ingen rabatt denna gång')

final_price = price * (100 - discount) / 100

print('Totala priset blir', final_price)


#print('Efter rabatter blir priset', final_price)