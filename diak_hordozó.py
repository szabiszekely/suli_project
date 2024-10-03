#hány felhasználó
#bekéri a diákok nevét és jegyét
#tárólás lista és tuple (diák + jegy)
lista = []


    

def diak_felvetel(tanulo_szama):
    for i in range(tanulo_szama):
        tup_1 = input("Kérem a diák nevét: ")
        try:
            tup_2 = int(input("Kérem az osztályzatát: "))
            if tup_2 > 5 or tup_2 < 1:
                print("5-nél nagyobb nem lehet!")
                szamok = tanulo_szama - 1
                diak_felvetel(tanulo_szama-szamok)
            else:
                tuple_ossz = (tup_1,tup_2)
                lista.append(tuple_ossz)
                print(lista)
        except:
            szamok = tanulo_szama - 1
            diak_felvetel(tanulo_szama-szamok)
        

def diakok_bekerese():
    try:
        tanulo_szama = int(input("Hány diákot tegyünk bele: "))
    except:
        diakok_bekerese()
    
    diak_felvetel(tanulo_szama)
    

def ossz_diak():
    print("\n")
    ujra = True
    while ujra:
        print("Szeretené e megtekinteni az összes diákot?")
        kerdes = input("I/N: ").upper()
        if kerdes == "I":
            ujra = False
            print("\n")
            for i in lista:
                print(f"Diák: {i[0]}, Osztályzat: {i[1]}")
        elif kerdes == "N":
            ujra = False
            print("\n")
            print("Müveletböl való kilépés!")
        else:
            print("Kérem írja újra!")

def atlag_diakok_jegye():
    print("\n")
    ujra = True
    ossz = 0
    while ujra:
        print('Szeretné e tudni az összes diák átlagát?')
        kerdes = input("I/N: ").upper()
        if kerdes == "I":
            ujra = False
            print("\n")
            for i in lista:
                ossz = ossz + i[1]
            atlag = ossz/len(lista)
            print(atlag)
        elif kerdes == "N":
            ujra = False
            print("\n")
            print("Müveletböl való kilépés!")
        else:
            print("Kérem írja újra!")

def minimum_es_maximum():
    print("\n")
    ujra = True
    while ujra:
        
        print('Szeretné e tudni a minimum és a maximum osztályzatott?')
        kerdes = input("I/N: ").upper()
        if kerdes == "I":
            ujra = False
            print("\n")
            jegyek=[]
            for i in lista:
                jegyek.append(i[1])
                
            minimum= min(jegyek)
            maximum= max(jegyek)
            print(f"A minimum jegy az: {minimum}; Míg a maximum jegy az: {maximum}!")
        elif kerdes == "N":
            ujra = False
            print("\n")
            print("Müveletböl való kilépés!")
        else:
            print("Kérem írja újra!")

def diak_torles():
    print("\n")
    ujra = True
    while ujra:
        print('Szeretné e törölni egy diákot?')
        kerdes = input("I/N: ").upper()
        if kerdes == "I":
            ujra = False
            print("\n")
            szamok = 0
            diakok_neve = []
            for i in lista:
                szamok += 1
                print(f"{szamok} Név: {i[0]}")
                diakok_neve.append(i)
            lista_szam = len(lista)
            diak_valasztas = True
            while diak_valasztas: 
                try:
                    valasztas = int(input("Válaszon egy diák számát: "))
                except:
                    print("Rossz input")
                valasztas -= 1
                if valasztas < 0:
                    print("\n")
                    print("Null és alatta nem egy opció! diák 1 lett ki választva")
                    szamok = 0
                    for i in lista:
                        szamok += 1
                        print(f"{szamok} Név: {i[0]}")
                elif valasztas >= lista_szam:
                    print("\n")
                    print("Diák száma nem lehet nagyobb a listánénál!")
                    szamok = 0
                    for i in lista:
                        szamok += 1
                        print(f"{szamok} Név: {i[0]}")
                else:
                    diak_valasztas = False
                    diak_nev = diakok_neve[valasztas]
                    print(f"{diak_nev[0]} Ki lett törölve!")
                    
                    lista.remove(diak_nev)
                    print(lista)
                
        elif kerdes == "N":
            ujra = False
            print("\n")
            print("Müveletböl való kilépés!")
        else:
            print("Kérem írja újra!")

diakok_bekerese()
ossz_diak()
atlag_diakok_jegye()
minimum_es_maximum()
diak_torles()