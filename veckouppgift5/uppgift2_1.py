#1a
def c_to_f(degree):
    if degree < -273.15:
        return None
    else:
        return degree * 9 / 5 + 32

grader = c_to_f(-273.13)
print(grader)

#Testdata:
#Ett ogiltigt värde: Tal mindre än nollpunkten (-300)
#Förväntat resultat: None

#Ett värde som inte är int eller float ('Hello')
#Förväntat resultat: TypeError ?

#En normal temperatur (0)
#Förväntat resultat: 32

#En temperatur nära nollpunkten (-273.17)
#Förväntat resultat: None

#En till temperatur nära nollpunkten (-273.13)
#Förväntat resultat: -459.634

#1b
degree < -273.15
degree >= -273.15

#1c
Verifiera att funktionen omvandlar temperaturen korrekt
Indata: degree = 100
Förväntat resultat: 212