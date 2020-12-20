from geometry import Geometry


class Section:
    def askgeo(self):
        h = float(input("indicare l'altezza della sezione di calcestruzzo H[mm]: "))
        b = float(input("indicare la base della sezione di calcestruzzo B[mm]: "))
        c = float(input("indicare il copriferro netto della sezione di calcestruzzo c[mm]: "))
        self.geometria = Geometry(h,b,c)

