import turtle as t


def rita_kvadrat(sida):


    for x in range(4):          #Gör allt i funktionen fyra gånger (4 sidor)
        t.backward(sida)
        t.left(90)              #Svänger 90 grader


    t.mainloop()                # Håll fönstret öppet tills man klickar på det



rita_kvadrat(100)               #Skickar med längd 100