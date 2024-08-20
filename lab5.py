import xml.etree.ElementTree as ET
import oracledb

def import_from_xml():
    selected_table = input("Wybierz tabelę, do której chcesz zaimportować dane: ")
    xml_file = input("Podaj nazwę pliku XML do importu: ")

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        conn = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
        cursor = conn.cursor()

        for record in root.findall("record"):
            values = []
            for column in record:
                values.append(column.text)
            placeholders = ":" + ", :".join(str(i + 1) for i in range(len(values)))
            query = f"INSERT INTO {selected_table} VALUES ({placeholders})"
            cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
        print("Dane zostały zaimportowane z pliku XML.")
    except Exception as e:
        print(f"Wystąpił błąd podczas importowania danych z pliku XML: {str(e)}")

def export_to_xml():
    selected_table = input("Wybierz tabelę, którą chcesz wyeksportować do pliku XML: ")
    xml_file = input("Podaj nazwę pliku XML do eksportu: ")

    conn = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()

    root = ET.Element("database")
    table_element = ET.SubElement(root, "table", name=selected_table)
    for row in rows:
        record = ET.SubElement(table_element, "record")
        for i, value in enumerate(row):
            column_name = cursor.description[i][0]
            column_value = str(value)
            ET.SubElement(record, column_name).text = column_value

    try:
        tree = ET.ElementTree(root)
        tree.write(xml_file)
        print("Eksport zakończony sukcesem.")
    except Exception as e:
        print(f"Wystąpił błąd podczas eksportu do pliku XML: {str(e)}")

    cursor.close()
    conn.close()

def add_record():
    selected_table = input("Wybierz tabelę, do której chcesz dodać rekord(rezerewacje, klienci, pracownicy): ")
    conn = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cursor = conn.cursor()

    if selected_table == "rezerwacje":
        try:
            id_rezerwacji = int(input("Podaj ID rezerwacji: "))
            data_przybycia = input("Podaj datę przybycia (RRRR-MM-DD): ")
            data_wyjazdu = input("Podaj datę wyjazdu (RRRR-MM-DD): ")
            klienci_id_klienta = int(input("Podaj ID klienta: "))
            pracownicy_id = int(input("Podaj ID pracownika: "))

            cursor.execute("INSERT INTO rezerwacje VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), TO_DATE(:3, 'YYYY-MM-DD'), :4, :5)",
                           (id_rezerwacji, data_przybycia, data_wyjazdu, klienci_id_klienta, pracownicy_id))
            conn.commit()
            print("Rekord dodany do tabeli 'rezerwacje'.")
        except ValueError:
            print("Nieprawidłowe dane. Spróbuj ponownie.")

    elif selected_table == "klienci":
        try:
            id_klienta = int(input("Podaj ID klienta: "))
            nazwisko = input("Podaj nazwisko: ")
            imie = input("Podaj imię: ")
            pesel = input("Podaj PESEL: ")
            paszport_covid = input("Czy posiada paszport COVID (T/N): ")
            nr_kontaktowy = input("Podaj numer kontaktowy: ")
            data_rejestracji_klienta = input("Podaj datę rejestracji klienta (RRRR-MM-DD): ")
            ilosc_osob = int(input("Podaj ilość osób: "))

            cursor.execute("INSERT INTO klienci VALUES (:1, :2, :3, :4, :5, :6, TO_DATE(:7, 'YYYY-MM-DD'), :8)",
                           (id_klienta, nazwisko, imie, pesel, paszport_covid, nr_kontaktowy, data_rejestracji_klienta, ilosc_osob))
            conn.commit()
            print("Rekord dodany do tabeli 'klienci'.")
        except ValueError:
            print("Nieprawidłowe dane. Spróbuj ponownie.")

    elif selected_table == "pracownicy":
        try:
            id_pracownika = int(input("Podaj ID pracownika: "))
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            data_zatrudnienia = input("Podaj datę zatrudnienia (RRRR-MM-DD): ")
            stanowisko_id = int(input("Podaj ID stanowiska: "))

            cursor.execute("INSERT INTO pracownicy VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)",
                           (id_pracownika, imie, nazwisko, data_zatrudnienia, stanowisko_id))
            conn.commit()
            print("Rekord dodany do tabeli 'pracownicy'.")
        except ValueError:
            print("Nieprawidłowe dane. Spróbuj ponownie.")

    else:
        print("Niepoprawny wybór tabeli.")

    cursor.close()
    conn.close()

while True:
    print("1. Importuj z pliku XML")
    print("2. Eksportuj do pliku XML")
    print("3. Dodaj rekord do tabeli")
    print("4. Wyjdź z programu")
    choice = input("Wybierz opcję: ")

    if choice == "1":
        import_from_xml()
    elif choice == "2":
        export_to_xml()
    elif choice == "3":
        add_record()
    elif choice == "4":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
