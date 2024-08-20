import oracledb
from oracle_insert import stanowisko, dostepnosc_pokoi, klienci, pracownicy, faktura, rezerwacje, pokoje, typ_pokoi, oplata, mieszkancy
from oracle_delete import delete_wszystko
from losoweFunkcje import dodaj_losowe_daty

def n_rekordow_do_tabel():
    
    n = int(input("Podaj liczbe rekordów do dodania do każdej z tabel w bazie danych: "))

    stanowisko(13)        #tabela słownikowa
    typ_pokoi()           #tabela słownikowa
    dostepnosc_pokoi(n)
    klienci(n)
    pracownicy(n)
    faktura(n)
    rezerwacje(n)
    pokoje(n)
    oplata(n)
    mieszkancy(n)
    print(f"\n\n Pomyślnie wykonane operację dodania wszystkich rekordów do bazy danych \n")
    
def tys_rekordow_do_tabel():
    
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    wybor = input("Wybierz tabele do której chcesz wprowadzić 1000 insertów. \n1. Rezerwacje \n2. Klienci \n3. Pracownicy \n")
    
    if wybor == '1': 
        cur = connection.cursor()
        l_data_przybycia, l_data_wyjazdu = dodaj_losowe_daty(1000)
        stanowisko(13)
        klienci(1)
        pracownicy(1)
        
        with open("insertplik.txt", "a") as f:
            for i in range(1000):
                data_przybycia = l_data_przybycia[i]
                data_wyjazdu = l_data_wyjazdu[i]
                
                randomInsert = f"INSERT INTO rezerwacje (id_rezerwacji, data_przybycia, data_wyjazdu, klienci_id_klienta, pracownicy_id)VALUES ({i}, {data_przybycia}, {data_wyjazdu}, 1, 1)"
                
                print(randomInsert)
                f.write(randomInsert + "\n")
                cur.execute(randomInsert)

            connection.commit()
            connection.close()
            
    elif wybor == '2':
        klienci(1000)
    
    elif wybor == '3':
        stanowisko(13)
        pracownicy(1000)


    print(f"\n\n Pomyślnie wykonane operację dodania wszystkich rekordów do bazy danych \n")

def n_rekordow_do_wybranej_tabeli():
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    wybor = input("Wybierz tabele do której chcesz wprowadzić n insertów. \n1. Rezerwacje \n2. Klienci \n3. Pracownicy \n")
    
    if wybor == '1':
        
        n = int(input("\nPodaj ile chcesz wprowadzić rekordów do tej tablicy\n")) 
        cur = connection.cursor()
        l_data_przybycia, l_data_wyjazdu = dodaj_losowe_daty(n)
        stanowisko(13)
        klienci(1)
        pracownicy(1)
        
        with open("insertplik.txt", "a") as f:
            for i in range(n):
                data_przybycia = l_data_przybycia[i]
                data_wyjazdu = l_data_wyjazdu[i]
                
                randomInsert = f"INSERT INTO rezerwacje (id_rezerwacji, data_przybycia, data_wyjazdu, klienci_id_klienta, pracownicy_id)VALUES ({i}, {data_przybycia}, {data_wyjazdu}, 1, 1)"
                
                print(randomInsert)
                f.write(randomInsert + "\n")
                cur.execute(randomInsert)

            connection.commit()
            connection.close()
            
    elif wybor == '2':
        n = int(input("\nPodaj ile chcesz wprowadzić rekordów do tej tablicy\n")) 
        
        klienci(n)
    
    elif wybor == '3':
        n = int(input("\nPodaj ile chcesz wprowadzić rekordów do tej tablicy\n")) 

        stanowisko(13)
        pracownicy(n)


    print(f"\n\n Pomyślnie wykonane operację dodania wszystkich rekordów do bazy danych \n")
    
default_user = "system"
default_password = "oracle"
default_host = "localhost"
default_port = 1521
default_sid = "xe"

def connect_to_database(user=default_user, password=default_password, host=default_host, port=default_port, sid=default_sid):
    connection = oracledb.connect(user=default_user, password=default_password, host=default_host, port=default_port, sid=default_sid)
    return connection

print("\n Zaloguj się do bazy danych \n")
user = input("Podaj login: ")
password = input("Podaj hasło: ")
host = input("Podaj host: ")
port = input("Podaj port: ")
sid = input("Podaj sid: ")


try:
    connection = connect_to_database(user, password, host, port, sid)
except oracledb.DatabaseError as e:
    print(f"Nie udało połączyć się z bazą, błąd: {e}")
    exit()
    
print("\nPomyślnie Połączono się z bazą danych \n")
wybor = 0

while wybor != '5':
    
    wybor = input("Wybierz opcję: \n1. Usuń wszystkie rekordy z bazy danych oraz plik .txt \n2. Dodaj n rekordów do bazy danych \n3. Dodaj 1000 rekordów do bazy danych \n4. Dodaj n rekordów do wybranej tablicy \n5. Wyjdź z programuy \n")

    if wybor == '1':
        delete_wszystko()
    elif wybor == '2':
        n_rekordow_do_tabel()
    elif wybor == '3':
        delete_wszystko()
        tys_rekordow_do_tabel()
    elif wybor == '4':
        n_rekordow_do_wybranej_tabeli()
    elif wybor == '5':
        exit()
    else:
        print("\nNiepoprawny wybór. Spróbuj ponownie \n")



connection.commit()
connection.close()