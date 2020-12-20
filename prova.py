from section import Section
# inizializzo delle variabili
i = 0
flag = True
sezione = []

while flag:
    risposta = input("creare una nuova sezione? (si/no) ")
    if risposta == "si":
        s = Section()
        sezione.append(s.askgeo())
        i = + 1
    else:
        flag = False

for n in range(i+1):
    area=sezione[n].geometria.area