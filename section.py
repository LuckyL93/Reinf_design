from geometry import Geometry
from concretetype import ConcreteType
from steeltype import SteelType


class Section:
    def askgeo(self):
        self.h = float(input("indicare l'altezza della sezione di calcestruzzo H[mm]: "))
        self.b = float(input("indicare la base della sezione di calcestruzzo B[mm]: "))
        self.c = float(input("indicare il copriferro netto della sezione di calcestruzzo c[mm]: "))
    def geometria(self):
        return Geometry(self.h,self.b,self.c)

    def askcls(self):
        self.fck = float(input("indicare il valore di fck del calcestruzzo utilizzato: "))
    def calcestruzzo(self):
        return ConcreteType(self.fck)

    def asksteel(self):
        self.fyk = float(input("indicare il valore di fck dell'acciaio: "))
    def acciaio(self):
        return SteelType(self.fyk)
