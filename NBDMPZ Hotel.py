class Hotel:
    def __init__(self,hotel_name ,hotel_address):
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
        self.lakosztaly_erkely  = lakosztaly_erkely
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

my_hotel = Hotel('NBDMPZ HOTEL', '1234 BP Egyetem tér 3')
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

my_foglalas = foglalalas_osztaly( 'NBDMPZ Hotel',  10, '2024.08.10','Kiss Józsi')
my_foglalas2 = foglalalas_osztaly ( 'NBDMPZ Hotel', 9, '2024.04.30.', 'Papp Pista' )
my_foglalas3 = foglalalas_osztaly ( 'NBDMPZ Hotel', 10, '2024.07.30.', 'Papp Pista' )
my_foglalas4 = foglalalas_osztaly ( 'NBDMPZ Hotel', 8, '2025.07.30.', 'Szabó Irén' )
my_foglalas5 = foglalalas_osztaly ( 'NBDMPZ Hotel',  7 , '2025.08.11.', 'Tóth Erika' )
my_foglalas6 foglalalas_osztaly ( 'NBDMPZ Hotel', 9, '2024.06.23.', 'Deák Boldizsárné' )
















my_lakosztaly= Hotelszoba("Lakosztály")
my_lakosztaly.hotelszoba_name = " CSILLAG "
my_lakosztaly.hotelszoba_price = 15000
my_lakosztaly.hotelszoba_num = 10



