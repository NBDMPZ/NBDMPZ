
from datetime import datetime

class Hotel:
    def __init__(self, hotel_name, hotel_address):
        self.hotel_name = hotel_name
        self.hotel_address = hotel_address

class Hotelszoba:
    def __init__(self, hotelszoba_type):
        self.hotelszoba_type = hotelszoba_type
        self.hotelszoba_name = ' '
        self.hotelszoba_price = 0
        self.hotelszoba_num = 0
class Lakosztaly(Hotelszoba):
    def __init__(self, lakosztaly_tajolas, lakosztaly_erkely):
        super().__init__('lakosztaly')
        self.lakosztaly_tajolas = lakosztaly_tajolas
        self.lakosztaly_erkely = lakosztaly_erkely
class standard(Hotelszoba):
    def __init__(self, hotelszoba_agyakszama):
        super().__init__('standard')
        self.hotelszoba_agyakszama = hotelszoba_agyakszama

class foglalalas_osztaly:
    def __init__(self, Hotel, szobaszam, datum, vendegneve):
        self.Hotel = Hotel
        self.szobaszam = szobaszam
        self.datum = datum
        self.vendegneve = vendegneve

my_hotel = Hotel('NBDMPZ HOTEL', '1234 BP Egyetem ter 3')
my_szoba1 = Lakosztaly('tengerre nezo','erkelyes')
my_szoba1.hotelszoba_name = 'Kredit'
my_szoba1.hotelszoba_price = 150000
my_szoba1.hotelszoba_num = 10

my_szoba2 = Lakosztaly('udvarra nezo','erkelyes')
my_szoba2.hotelszoba_name = 'Neptun'
my_szoba2.hotelszoba_price = 130000
my_szoba2.hotelszoba_num = 9

my_szoba3 = standard( 1 )
my_szoba3.hotelszoba_name = 'NMS'
my_szoba3.hotelszoba_price = 50000
my_szoba3.hotelszoba_num = 8

my_szoba4 = standard( 2 )
my_szoba4.hotelszoba_name = 'ZH'
my_szoba4.hotelszoba_price = 75000
my_szoba4.hotelszoba_num = 7

my_foglalas = []
my_foglalas.append(foglalalas_osztaly( 'NBDMPZ Hotel',  10, '2024.08.10','Kiss Jozsi'))
my_foglalas.append(foglalalas_osztaly( 'NBDMPZ Hotel', 9, '2024.05.16', 'Papp Pista'))
my_foglalas.append(foglalalas_osztaly( 'NBDMPZ Hotel', 10, '2024.07.30', 'Papp Pista'))
my_foglalas.append(foglalalas_osztaly( 'NBDMPZ Hotel', 8, '2025.07.30', 'Szabó Iren'))
my_foglalas.append(foglalalas_osztaly( 'NBDMPZ Hotel',  7 , '2025.08.11', 'Toth Erika'))
my_foglalas.append(foglalalas_osztaly ( 'NBDMPZ Hotel', 9, '2024.06.23', 'Deak Boldizsarne'))



def foglalt(datum3, szoba3):
    foglalte=False
    for foglalas in my_foglalas:
        if datum3 == foglalas.datum and str(szoba3) == str(foglalas.szobaszam):
           foglalte=True
    return foglalte



def listazas():
    for foglalas in my_foglalas:
        print("Nev: "+foglalas.vendegneve + " Szobaszam: "+str(foglalas.szobaszam) + " Datum: "+str(foglalas.datum))


def ujfoglalas(vendeg, datum, szoba):
    if foglalt(datum, szoba):
        return print("Szoba foglalt")
    else:
        my_foglalas.append(foglalalas_osztaly( 'NBDMPZ Hotel',szoba, datum, vendeg))
        if(szoba==10):
            szobaar=my_szoba1.hotelszoba_price
        elif(szoba==9):
            szobaar=my_szoba2.hotelszoba_price
        elif(szoba==8):
            szobaar=my_szoba3.hotelszoba_price
        elif(szoba==7):
            szobaar=my_szoba4.hotelszoba_price
        else:
            szobaar= 0
        return print("Foglalas letrehozva.Szobaar:" +str(szobaar))

def lemondas(datum2, szoba2):
    if foglalt(datum2, szoba2):
        for foglalas in my_foglalas:
            if datum2 == foglalas.datum and str(szoba2) == str(foglalas.szobaszam):
                my_foglalas.remove(foglalas)
        print("Szoba lemondva")
    else:
        return print("Nincs ilyen foglalas")



def Menu():
    while True:
        print("\nVálassz Menupontot:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        menu = input("Valasztott Menupont: ")
        if menu == "1":
            nev=input("Kérem adja meg a nevét:")
            szobasz = input("Szobaszam: ")
            datum = input("Foglalas datuma (EEEE.MM.DD) formátumban: ")
            datum1 = datetime.strptime(datum, "%Y.%m.%d")
            if datum1 < datetime.now():
                print("\nRossz dátum! A foglalás csak jövőbeni időpontra lehetséges.")
            elif szobasz != "7" and szobasz != "8" and szobasz != "9" and szobasz != "10":
                print("Nincs ilyen szoba")
            else:
                ujfoglalas(nev,datum, int(szobasz))
        elif menu == "2":
            szobasz = input("Adja meg a lemondani kívánt szobaszamot: ")
            datum = input("Foglalas datuma (EEEE.MM.DD) formátumban: ")
            lemondas(datum,int(szobasz))
        elif menu == "3":
            listazas()
        elif menu == "4":
            break

        else:
            print("Hibás menupont")



Menu()

















