import oracledb
import random
import datetime
import string
from faker import Faker
from losoweFunkcje import random_id, lista_losowych_dat, losowy_nip, losowy_numer_kontaktowy, generate_pesel, dodaj_losowe_daty


def dostepnosc_pokoi(n):
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()

    lista_id = random_id(n+1)
    lista_dat = lista_losowych_dat(n)
    l = ['T', 'F']
    
    print(cur.execute(f"SELECT MAX(id_dostepnosci_pokoju) FROM dostepnosc_pokoi"))
    result = cur.fetchone()
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])

    lista_id = random_id(n+min)
    lista_dat = lista_losowych_dat(n+min)
    l = ['T', 'F']
    
    with open("insertplik.txt", "a") as f:
        if n >= 6:
            for i in range(min, min + n):
                
                id = lista_id[i+1]    
                data =  lista_dat[i+1]
                dostepnosc_pokoju = random.choice(l)
                
            
                randomInsert = f"INSERT INTO dostepnosc_pokoi (id_dostepnosci_pokoju, data_dostepnosci, dostepnosc_pokoju)VALUES({id}, {data}, '{dostepnosc_pokoju}')"
                f.write("\n" + randomInsert + "\n")
                print(randomInsert)
                cur.execute(randomInsert)

            connection.commit()
            connection.close()
        else:
                for i in range(min, 6):
                  
                    id = lista_id[i+1]    
                    data =  lista_dat[i+1]
                    dostepnosc_pokoju = random.choice(l)
                    
                
                    randomInsert = f"INSERT INTO dostepnosc_pokoi (id_dostepnosci_pokoju, data_dostepnosci, dostepnosc_pokoju)VALUES({id}, {data}, '{dostepnosc_pokoju}')"
                    f.write("\n" + randomInsert + "\n")
                    print(randomInsert)
                    cur.execute(randomInsert)

                connection.commit()
                connection.close()
  
def faktura(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()

    print(cur.execute(f"SELECT MAX(numer_dokumentu) FROM faktura"))
    result = cur.fetchone()
    
    if result is None or result[0] is None:
        min = 0
    else:
        min = result[0]
        print(min)
        last_three_digits = min[-7:]  # Extract last 3 digits using string slicing
        min = int(last_three_digits)  # Convert extracted string to integer

    
    fake = Faker('pl_PL')
    lista_id = random_id(n+1)
    lista_nip = losowy_nip(n+1)
    l =['T', 'F']
    rok = datetime.date.today().year
    numer_kontrolny = [str(num).zfill(3) for num in range(min+1, min+n+1)]
    listaw_dostawcow = [' Sp. z o.o.', ' Sp. j.', ' S.A.', ' Sp.p.',' Sp.k.',' S.K.A.']
    nazwa = '{}{}{}'.format(random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase))
    lista_rodzaj_wydatku = ['Koszty hotelowe', 'Pobyt w hotelu', 'Noclegi w hotelu', 'Hotel - nocleg']
    lista_dat = lista_losowych_dat(n+1)
    

    with open("insertplik.txt", "a") as f:
        for i in range(0, n):
            
            nazwa = '{}{}{}'.format(random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase))

            data_wystawienia = lista_dat[i]
            dostawca = nazwa + random.choice(listaw_dostawcow)
            id_klienta = random.randint(1, n)
            adres = fake.address()
            nip = lista_nip[i]
            metoda_platnosci = random.choice(l)
            zaplacono_calosc = random.choice(l)
            kwota = random.randint(1000, 25000)
            rodzaj_wydatku = random.choice(lista_rodzaj_wydatku)
            
            randomInsert = f"INSERT INTO faktura (numer_dokumentu, dostawca, adres, nip, data_wystawienia_faktury, metoda_platnosci_gotowka, zaplacono_calosc, rodzaj_wydatku, kwota, klienci_id_klienta) VALUES ('FV/{rok}/{numer_kontrolny[i]}', '{dostawca}', '{adres}', {nip}, {data_wystawienia},  '{metoda_platnosci}', '{zaplacono_calosc}', '{rodzaj_wydatku}', {kwota}, {id_klienta})"
            
            print(randomInsert)
            f.write("\n" + randomInsert + "\n")
            cur.execute(randomInsert)

        connection.commit()
        connection.close()

def klienci(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()

    print(cur.execute(f"SELECT MAX(id_klienta) FROM klienci"))
    result = cur.fetchone()
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])

    fake = Faker('pl_PL')

    l = ['T', 'F']
    lista_dat = lista_losowych_dat(n+min)
    lista_id = random_id(n+min)
    lista_numerow_kontaktowych = losowy_numer_kontaktowy(n+min)
    lista_pesel = generate_pesel(n+min)
    
    with open("insertplik.txt", "a") as f:
        for i in range(0, n):
            
            imie = fake.first_name()
            nazwisko =fake.last_name()
            data_rejestracji_klienta = lista_dat[i]
            nr_kontaktowy = lista_numerow_kontaktowych[i]
            paszport_covid = random.choice(l)
            id = lista_id[min+i+1]
            ilosc_osob = random.randint(1, 5)
            pesel = lista_pesel[i]
        
            randomInsert = f"INSERT INTO klienci (id_klienta, nazwisko, imie, pesel, paszport_covid, nr_kontaktowy, data_rejestracji_klienta, ilosc_osob) VALUES ({id}, '{nazwisko}', '{imie}', '{pesel}', '{paszport_covid}',  '{nr_kontaktowy}', {data_rejestracji_klienta}, {ilosc_osob})"
            
            print(randomInsert)
            f.write("\n" + randomInsert + "\n")
            cur.execute(randomInsert)

        connection.commit()
        connection.close()

def mieszkancy(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()
    
    print(cur.execute(f"SELECT MAX(id_mieszanca) FROM mieszkancy"))
    result = cur.fetchone()
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])


    l_data_zameldowania, l_data_wymeldowania = dodaj_losowe_daty(n+min)

    
    lista_id = random_id(n+min)
    with open("insertplik.txt", "a") as f:    
        for i in range(min, min+n):
        
            data_zameldowania = l_data_zameldowania[i]
            data_wymeldowania = l_data_wymeldowania[i]        
            id = lista_id[i+1]
            ilosc_mieszkancow = random.randint(1, 10)
            
            randomInsert = f"INSERT INTO mieszkancy (id_mieszanca, data_zameldowania, data_wymeldowania, pokoje_id_pokoju, rezerwacje_id_rezerwacji, ilosc_mieszkancow) VALUES ({id}, {data_zameldowania}, {data_wymeldowania}, {id}, {id}, {ilosc_mieszkancow})"

            
            f.write("\n" + randomInsert + "\n")
            print(randomInsert)
            cur.execute(randomInsert)
            
        connection.commit()
        connection.close()

def oplata(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()

    print(cur.execute(f"SELECT MAX(id) FROM opłata"))
    result = cur.fetchone()
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])


    data = lista_losowych_dat(n+min)
    podatek_l = ['T', 'N']
    zaliczka_l = ['T', 'N']
    lista_id = random_id(n+min)

    with open("insertplik.txt", "a") as f:     
        for i in range(min, n+min):
            
            data_wykonania_oplaty = data[i]
            zaliczka_cena = random.randint(50, 1000)
            podatek = random.choice(podatek_l)
            zaliczka = random.choice(zaliczka_l)
            id = lista_id[i+1]
            kwota = random.randint(500, 70000)
        
            randomInsert = f"INSERT INTO opłata (id, kwota, data_wykonania_oplaty, zaliczka, zaliczka_cena, podatek, rezerwacje_id_rezerwacji) VALUES ({id}, {kwota}, {data_wykonania_oplaty}, '{zaliczka}', {zaliczka_cena}, '{podatek}', {id})"

            f.write("\n" + randomInsert + "\n")
            print(randomInsert)
            cur.execute(randomInsert)
            
        connection.commit()
        connection.close()

def pokoje(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()
    
    print(cur.execute(f"SELECT MAX(id_pokoju) FROM pokoje"))
    result = cur.fetchone()
    
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])

    lista_id = random_id(n+min)
    lista_typow_pokoi = ['pokój jednoosobowy', 'pokój dwuosobowy', 'pokój trzyosobowy', 'apartament', 'pokój rodzinny', 'studio']
    
    with open("insertplik.txt", "a") as f:    
        for i in range(n):
                
            typ = random.choice(lista_typow_pokoi)
            id = lista_id[i+1]
            
            randomInsert = f"INSERT INTO pokoje (id_pokoju, numer_pokoju, cena, dostepnosc_pokoi_id_dostepnosci_pokoju, typ_pokoi_typ_pokoi)VALUES ({id+min}, {random.randint(60, 600)}, {random.randint(500, 7000)}, {id+min}, '{typ}')"
                
            print(randomInsert)
            f.write("\n" + randomInsert + "\n")
            cur.execute(randomInsert)
                
        connection.commit()
        connection.close()

def pracownicy(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()
    fake = Faker('pl_PL')
    
    print(cur.execute(f"SELECT MAX(id) FROM pracownicy"))
    result = cur.fetchone()
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])


    lista_dat = lista_losowych_dat(n+min)
    lista_id = random_id(n+min)

    with open("insertplik.txt", "a") as f:        
        for i in range(0, n):
            
            imie = fake.first_name()
            nazwisko =fake.last_name()
            data_rejestracji_pracownika = lista_dat[i]
            id = lista_id[min+i+1]
            stanowisko_id = random.randint(0, 12) 
            randomInsert = f"INSERT INTO pracownicy (id, imie, nazwisko, data_zatrudnienia, stanowisko_id) VALUES ({id}, '{imie}', '{nazwisko}',  {data_rejestracji_pracownika}, {stanowisko_id})"
            
            print(randomInsert)
            f.write("\n" + randomInsert + "\n")
            cur.execute(randomInsert)
            
        connection.commit()
        connection.close()

def rezerwacje(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()
    
    print(cur.execute(f"SELECT MAX(id_rezerwacji) FROM rezerwacje"))
    result = cur.fetchone()
    
    if result[0] is None:
        min = 0
    else:
        min = int(result[0])
        
    print(cur.execute(f"SELECT MAX(id) FROM pracownicy"))
    result = cur.fetchone()
    
    if result[0] is None:
        min_pracownicy = 0
    else:
        min_pracownicy = int(result[0])

    print(cur.execute(f"SELECT MAX(id_klienta) FROM klienci"))
    result = cur.fetchone()
    
    if result[0] is None:
        min_klienci = 0
    else:
        min_klienci = int(result[0])
    
    l_data_przybycia, l_data_wyjazdu = dodaj_losowe_daty(n+min)
    lista_id = random_id(n+min)
    
    
    with open("insertplik.txt", "a") as f:
        for i in range(n):
            
            data_przybycia = l_data_przybycia[i]
            data_wyjazdu = l_data_wyjazdu[i]
            id = lista_id[i+1]
        
            randomInsert = f"INSERT INTO rezerwacje (id_rezerwacji, data_przybycia, data_wyjazdu, klienci_id_klienta, pracownicy_id)VALUES ({id+min}, {data_przybycia}, {data_wyjazdu}, {random.randint(1, min_klienci)}, {random.randint(1, min_pracownicy)})"
            
            print(randomInsert)
            f.write(randomInsert + "\n") 
            cur.execute(randomInsert)
            
        connection.commit()
        connection.close()

def stanowisko(n):
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()

    print(cur.execute(f"SELECT MAX(id) FROM stanowisko"))
    result = cur.fetchone()
    
    if result[0] == 12:
        return
    else:
        
        stanowiska = ['kierownik/czka', 'kucharz', 'pokojówka','zastepca kierownika', 'barman/ka','kelner/ka', 'recepcjonistka/a', 'sprzątaczka', 'kierownik recepcji', 'kierownik kuchni', 'kierownik baru', 'kierownik sprzątania', 'kierownik pokoi']
        lista_id = random_id(n)
        
        with open("insertplik.txt", "a") as f:    
            for i in range(len(stanowiska)):
            
                stanowisko = stanowiska[i]
                id = lista_id[i]
        
                randomInsert = f"INSERT INTO stanowisko (id, stanowisko) VALUES ({id}, '{stanowisko}')"

                f.write("\n" + randomInsert + "\n")
                print(randomInsert)
                cur.execute(randomInsert)
            
        connection.commit()
        connection.close()

def typ_pokoi():
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()
    
    print(cur.execute(f"SELECT typ_pokoi FROM typ_pokoi"))
    result = cur.fetchone()
    print(result)
    if result is not None:
        return
    else:
        with open("insertplik.txt", "a") as f:

            cur.execute(f"INSERT INTO typ_pokoi VALUES ('pokój jednoosobowy', 1)")
            print("INSERT INTO typ_pokoi VALUES ('pokój jednoosobowy', 1)")
            f.write("\n" + "INSERT INTO typ_pokoi VALUES ('pokój jednoosobowy', 1)" + "\n")
            
            cur.execute(f"INSERT INTO typ_pokoi VALUES ('pokój dwuosobowy', 2)")
            print("INSERT INTO typ_pokoi VALUES ('pokój dwuosobowy', 2)")
            f.write("\n" + "INSERT INTO typ_pokoi VALUES ('pokój dwuosobowy', 2)" + "\n")
                
            cur.execute(f"INSERT INTO typ_pokoi VALUES ('pokój trzyosobowy', 3 )")
            print("INSERT INTO typ_pokoi VALUES ('pokój trzyosobowy', 3)")
            f.write("\n" + "INSERT INTO typ_pokoi VALUES ('pokój trzyosobowy', 3)" + "\n")
            
            cur.execute(f"INSERT INTO typ_pokoi VALUES ('apartament', 2 )")
            print("INSERT INTO typ_pokoi VALUES ('apartament', 2 )")
            f.write("\n" + "INSERT INTO typ_pokoi VALUES ('apartament', 2 )" + "\n")
            
            cur.execute(f"INSERT INTO typ_pokoi VALUES ('pokój rodzinny', 4 )")
            print("INSERT INTO typ_pokoi VALUES ('pokój rodzinny', 4 )")
            f.write("\n" + "INSERT INTO typ_pokoi VALUES ('pokój rodzinny', 4 )" + "\n")
            
            cur.execute(f"INSERT INTO typ_pokoi VALUES ('studio', 10 )")
            print("INSERT INTO typ_pokoi VALUES ('studio', 10 )")
            f.write("\n" + "INSERT INTO typ_pokoi VALUES ('studio', 10 )" + "\n")
        
        
    connection.commit()
    connection.close()