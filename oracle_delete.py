import oracledb
import os
def delete_wszystko():
    connection = oracledb.connect(user="system", password="oracle", host="localhost", port=1521, sid="xe")
    cur=connection.cursor()
    
    delete = [
    
    "DELETE FROM faktura",
    "DELETE FROM opłata",
    "DELETE FROM mieszkancy",
    "DELETE FROM rezerwacje",
    "DELETE FROM pracownicy",
    "DELETE FROM klienci",
    "DELETE FROM pokoje",
    "DELETE FROM stanowisko",
    "DELETE FROM dostepnosc_pokoi",
    "DELETE FROM typ_pokoi",
    ]   
    
    for deletes in delete:
        #print(deletes)        
        cur.execute(deletes)
        
        
    print("\n\n Pomyślnie wykonane operację usunięcia wszystkich rekordów z bazy danych \n")
    
    filename = "insertplik.txt"

    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")
        
    connection.commit()
    connection.close()
