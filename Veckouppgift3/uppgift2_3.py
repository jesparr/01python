#3a
filmer = ['Scarface', 'Star Wars', 'Pulp Fiction', 'Apornas planet', 'Forrest Gump'] #Skapar och skriver ut lista med filmer
print(filmer)

#3b
filmer.append('Fellowship of the ring')                           #Lägger till film i slutet av lista
print(filmer)
#3c
filmer.insert(0, 'The two towers')                 #Lägger till Two Towers i början av lista, index 0
print(filmer)
#3d
print(filmer.index('Fellowship of the ring'))                     #Skriver ut vilket index Fellowship of the ring har

#3e
filmer.remove('Star Wars')                                        #Tar bort Star Wars ur listan
print(filmer.index('Fellowship of the ring'))                     #Skriver sen ut vilket index LOTR har

#3f
print(len(filmer))                                                #Skriver ut längden på listan

#3g
filmer.reverse()                                                  #Vänd på listan och skriv ut
print(filmer)

#3h
filmer.sort()                                                     #Sortera listan och skriv ut
print(filmer)
