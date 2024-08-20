import datetime
import random

def dodaj_losowe_daty(n, data_przybycia_poprzedniej_rezerwacji=None):
    # pobieramy dzisiejszą datę
    dzisiaj = datetime.date.today()
    
    # jeśli jest podana data poprzedniej rezerwacji, parsujemy ją do formatu datetime.date
    if data_przybycia_poprzedniej_rezerwacji:
        data_przybycia_poprzedniej_rezerwacji = datetime.datetime.strptime(data_przybycia_poprzedniej_rezerwacji, '%Y-%m-%d').date()
    
    # ustawiamy minimalną datę przybycia jako dzień po poprzedniej rezerwacji lub dzisiejszą datę, jeśli nie ma poprzedniej rezerwacji
    if data_przybycia_poprzedniej_rezerwacji:
        minimalna_data_przybycia = max(dzisiaj, data_przybycia_poprzedniej_rezerwacji + datetime.timedelta(days=1))
    else:
        minimalna_data_przybycia = dzisiaj
        
    # tworzymy listy na daty przyjazdu i wyjazdu
    daty_przyjazdu = []
    daty_wyjazdu = []
    
    for i in range(n+1):
        # ustawiamy minimalną datę wyjazdu jako 4 dni po minimalnej dacie przybycia
        minimalna_data_wyjazdu = minimalna_data_przybycia + datetime.timedelta(days=4)

        # ustawiamy maksymalną datę wyjazdu jako 14 dni po minimalnej dacie przybycia
        maksymalna_data_wyjazdu = minimalna_data_przybycia + datetime.timedelta(days=14)

        # losujemy datę wyjazdu z przedziału <minimalna_data_wyjazdu, maksymalna_data_wyjazdu>
        data_wyjazdu = datetime.date.fromordinal(
            minimalna_data_wyjazdu.toordinal() + 
            int((maksymalna_data_wyjazdu - minimalna_data_wyjazdu).days * random.random()))

        # dodajemy daty przyjazdu i wyjazdu do list
        daty_przyjazdu.append("TO_DATE('" + minimalna_data_przybycia.strftime('%Y-%m-%d') + "', 'YYYY-MM-DD')")
        daty_wyjazdu.append("TO_DATE('" + data_wyjazdu.strftime('%Y-%m-%d') + "', 'YYYY-MM-DD')")

        # ustawiamy minimalną datę przybycia na dzień po daty wyjazdu
        minimalna_data_przybycia = data_wyjazdu + datetime.timedelta(days=1)
    
    # zwracamy listy dat przybycia i wyjazdu
    return daty_przyjazdu, daty_wyjazdu

def lista_losowych_dat(n):
    start_date = '2023-04-01'  # Set a start date
    dates = []  # Create an empty list to store the dates

    for i in range(n+2+100):
        # Generate a random number of days to add to the previous date
        days = random.randint(1, 10)
        # Convert the start date to a datetime object
        current_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        # Add the random number of days to the current date
        current_date += datetime.timedelta(days=days)
        # Convert the current date back to a string in the desired format
        date_str = "TO_DATE('{}', 'YYYY-MM-DD')".format(current_date.strftime('%Y-%m-%d'))
        # Append the date string to the list of dates
        dates.append(date_str)
        # Set the start date to the current date for the next iteration
        start_date = current_date.strftime('%Y-%m-%d')

    
    return dates

def random_phone_num_generator():
    
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 998)).zfill(3))
    
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 998)).zfill(3))
        
    return '{}-{}-{}'.format(first, second, last)

def losowy_numer_kontaktowy(n):
    l = []
    for i in range(0, n+1+100):
        l.append(random_phone_num_generator())
    
    return l
        
def random_id(n):
    id = []    
    
    for i in range(n+2+100):
        id.append(i)
        
    return id    

def generate_pesel(n):
    pesel = ""
    l = []
   
   
    for i in range(n+1+100):
        pesel = ""
        for i in range(0, 11):
            pesel += str(random.randint(0, 9))
            
        l.append(pesel)
    return l

def losowy_nip(n):
    nip = ""
    l = []
   
   
    for i in range(n+100):
        nip = ""
        for i in range(0, 10):
            nip += str(random.randint(0, 9))
            
        l.append(nip)
    return l

