from section import Section
# inizializzo delle variabili
i = 0
flag = True
sezione = []

while flag:
    risposta = input("creare una nuova sezione? (si/no) ")
    if risposta == "si":
        s = Section()
        print("DEFINIZIONE DELLA GEOMETRIA")
        s.askgeo()
        sezione.append(s.geometria())
        print("DEFINZIONE DEL TIPO DI CALCESTRUZZO")
        s.askcls()
        sezione.append(s.calcestruzzo())
        print("DEFINIZIONE DEL TIPO DI ACCIAIO")
        s.asksteel()
        sezione.append(s.acciaio())
        i = + 1
    else:
        flag = False

for n in range(i+1):
    print(sezione[n].altezza)
    print(sezione[n].base)
    print(sezione[n].area)