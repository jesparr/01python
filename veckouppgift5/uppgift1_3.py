vowels = 'aeiouyåäö'                 # Här skapar jag en variabel med alla vokaler

def count_vowels(ord):
    count = 0                       # Count börjar på 0
    for bokstav in ord.lower():     # Räknar hur många av bokstäverna i argumentet på rad 13 som finns med i 'vowels'
        if bokstav in vowels:       # variabeln och gör alla bokstäver till gemener
            count += 1              # Ökar count med 1 tills hela ordet är kört i loopen
    return count



def test_count_vowels():
    actual = count_vowels('APaAa')  #Testar att räkna antal vokaler samt att se om den räknar samma vokal flera ggr
    expected = 4                    # Testar även case sensitivity
    assert actual == expected

def test_count_all_vowels():
    actual = count_vowels(vowels)   # Räknar alla vokaler som ligger i variabeln vowels och ser om det är 9st
    expected = 9
    assert actual == expected



def test_no_vowels():
    assert count_vowels('qwrt') == 0
    assert count_vowels('Tt') == 0
    assert count_vowels('123 123') == 0
    assert count_vowels('') == 0

#Tips 1: kan funktionen hitta någon vokal, över huvud taget?
#Tips 2: kan den räkna alla vokaler?
#Tips 3: kan den räkna samma vokal om den förekommer flera gånger?
#Tips 4: klarar den både stora och små bokstäver?