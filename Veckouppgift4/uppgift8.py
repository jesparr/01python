listan = ['a', 'b', 3.14]

def punktlista(listan):
    if listan == []:
        print('Listan är tom')
    else:
        print(f'Listan har {len(listan)} element')
        for i in enumerate(listan, start=1):                #Får inte listan att skriva ut punktlista utan parenteser hur jag än gör tyvärr
            print(i)

punktlista(listan)


