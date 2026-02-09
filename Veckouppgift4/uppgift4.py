lista = [1, 2, 3, True ,5 ,'Hello']

lista2 = ['Jesper', 'Maria', 'William']     #Gjorde två listor bara för att själv testa och se ifall jag kunde återanvända funktionen så den kunde ta emot vilken lista som helst

def last(y):
    return y[-1]

sista = last(lista)
print(sista)

andralistan = last(lista2)
print(andralistan)