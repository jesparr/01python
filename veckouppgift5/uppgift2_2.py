def count_words(sentence):
    sentence = str(sentence)    # omvandlar inmatning till str
    sentence = sentence.strip() # tar bort mellanslag före och efter strängen


    if sentence == "":          # om strängen är tom, returnera 0
        return 0

    ord = sentence.split()      # delar upp strängen i ord

    return len(ord)             # räknar antal ord




def test_count_words():
    assert count_words('hej') == 1
    assert count_words('hej san') == 2
    assert count_words('hej san Jesper') == 3
    assert count_words('') == 0
    assert count_words('   ') == 0
    assert count_words(' hej') == 1
    assert count_words(' hej ') == 1
    assert count_words('hej  jesper') == 2
    assert count_words('hej jag är 1 människa !') == 6






# Krav:
# Datatyp för returvärde:                                 AK: Funktionen ska returnera ett heltal som räknat ut antal ord i strängen
# TC01: Ett ord - Indata: hej            Expected: 1
# TC02: Två ård - Indata: hej san        Expected: 2
# TC03: Tre ord - Indata: hej san jesper Expected: 3

# Hantering av tomma strängar                             AK: Tomma strängar ska returnera 0, inte krascha funktionen
# TC04: Tom sträng - Indata: ''                 Expected: 0
# TC05: Tom sträng med endast mellanslag '  '   Expected: 0

# Mellanslag skall exkluderas i beräkningen av ord        AK: Mellanslag ska inte räknas som ord
# TC06: Mellanslag före ord.            Indata: ' hej'          Expected: 1
# TC08: Mellanslag före och efter ord.  Indata:' hej '          Expected: 1
# TC09: Flera mellanslag mellan ord.    Indata: 'hej  jesper'   Expected: 2

# Inmatningsformat (datatyp)                              AK: Funktionen skall kunna ta emot bokstäver, tecken eller siffror
# TC10: Inmatning - Indata: 'hej jag är 1 människa!'            Expected: 6

