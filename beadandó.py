import string
gyumolcsok = ["alma","banan","citrom","afonya","eper"]
for gyumolcs in gyumolcsok:
   if gyumolcs.startswith("a"):
    print(gyumolcs)


gyumolcsok = ["alma","banan","citrom","afonya","eper"]
gyumolcsoksorba=sorted(gyumolcsok)
for gyumolcs in gyumolcsoksorba:
    print(gyumolcs)


def osszead(a, b):
    return a-b

x=osszead(2,3)

print(x)



a = 5
print(type(a))
x = {1: "one", 2: "two", 3: "three"}
print(type(x))
tesztnev = "alma"
print(tesztnev)

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

class





my_lakosztaly= Hotelszoba("Lakosztály")
my_lakosztaly.hotelszoba_name = " CSILLAG "
my_lakosztaly.hotelszoba_price = 15000
my_lakosztaly.hotelszoba_num = 10



