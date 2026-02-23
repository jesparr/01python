class Product:                      # Här skapar vi själva "ritningen". Ordet class talar om för Python att allt som följer (och är indraget)
                                    # tillhör mallen för vad en Product är och kan göra.
    """Representerar produkter som kan visas i en webbshop."""

    name = ""                       # Dessa kallas klassattribut. De sätter standardvärden för alla produkter.
    price = 0                       # I praktiken kommer dessa ofta att skrivas över av de värden vi skickar in senare,
    count_in_stock = 0              # men de fungerar som en sorts deklaration av vad en produkt ska innehålla.

    def __init__(self, name, price, count_in_stock):
        # __init__ är konstruktor för klassen
        self.name = name
        self.price = price
        self.count_in_stock = count_in_stock

    def print_info(self):
        print(f"{self.name} kostar {self.price} och det finns {self.count_in_stock} stycken i lager")

skis = Product(name="Skidor", price=600, count_in_stock=15)
#ski_boots = Product(name="Pjäxor", price=800, count_in_stock=2)

skis.print_info()
#ski_boots.print_info()