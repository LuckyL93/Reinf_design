from section import Section
# inizializzo delle variabili
i = 0
flag = True
sezione = []

while flag:
    risposta = input("creare una nuova sezione [numero "+str(i+1)+"] (si/no) ")
    if risposta == "si":
        s = Section()
        sezione.append(s)
        print("DEFINIZIONE DELLA GEOMETRIA [SEZIONE NUMERO "+str(i+1)+"]")
        s.askgeo()
        s.geometria()
        #sezione.append(s.geometria())
        print("DEFINZIONE DEL TIPO DI CALCESTRUZZO [SEZIONE NUMERO "+str(i+1)+"]")
        s.askcls()
        s.calcestruzzo()
        #sezione.append(s.calcestruzzo())
        print("DEFINIZIONE DEL TIPO DI ACCIAIO [SEZIONE NUMERO "+str(i+1)+"]")
        s.asksteel()
        s.acciaio()
        #sezione.append(s.acciaio())
        i = i + 1
    else:
        flag = False


for n in range(i):
    print(sezione[n].geometria().area)
    print(sezione[n].calcestruzzo().fcd)
    print(sezione[n].acciaio().fyd)