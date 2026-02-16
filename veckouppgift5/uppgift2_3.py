#Funktionen ska ta en lista med tal och returnera medianen

# Krav: Hantering av tom lista                    AK: Vid tom lista skall funktionen returnera none
# Krav: Osorterad lista                           AK: Om talen inte är i storleksordning skall funktionen ändå räkna ut rätt
# Krav: Ett element                               AK: Om listan innehåller ett element, returnera det elementet
# Krav: Jämnt antal element                       AK: Funktionen skall returnera medelvärdet av de två mellersta elementen
# Krav: Listan skall hantera både float och int   AK: Användaren skall kunna skriva in både float och int

def find_median(numbers):
    sorted_list = sorted(numbers)
    a = len(sorted_list)
    mellan = a // 2

    if a % 2 == 0:
        return sorted_list[mellan]