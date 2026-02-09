#1a
def foo(t):
    print("test")

foo("hej")                      #Parametern t används aldrig i funktionen, kommer alltid skriva ut test oavsett argument när man anropar

#1b
def fun1(x, y):
    return x * y                #Funktionen anropas aldrig utan skriver bara ut två integers

print(3, 5)

#1c
def fun1(x, y):
    return x * y                #Funktionen anropas med argumenten 3 och 5, kommer då skriva ut 15

print(fun1(3, 5))

#1d
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

#1e
a = 5
def fun3(a):
    a += 1

a += 2                          #Finns ingen return inuti funktionen så att inget lämnar den, det ökas bara på med 2 på rad 33 och sen skriver ut
print(a)

#1f
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);            #Här används funktionen foo, alltså 2*i*i, där i blir 3. Alltså 2*3*3 som blir 18.
print(a)


#1g Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
def is_number(x):
    if isinstance(x, int):      #True returneras om en int eller float används som argument i is_number, vilket görs i båda fallen på rad 55 och 56
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

#1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(average_words)

#1i En uppgift i tre delar:
#Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
#Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
#Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])