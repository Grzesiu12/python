nowa_liczba = 0
nastepna = 0
liczby = []
ilosc_liczb = 0
while(True):
    #liczby = [int((input("podaj liczbe ")))]
    nastepna = int(input("czy chcesz podać następną liczbę "))
    if nastepna == 1:
        ilosc_liczb = ilosc_liczb + 1
        nowa_liczba = int(input("podaj liczbe "))
        liczby.append(nowa_liczba)
        print(liczby)
    if nastepna == 2:
        print(liczby)
        liczbaMin = min(liczby)
        print(liczbaMin)
        for nwd in range(liczbaMin, 0, -1):
            czy_nwd = True
            for liczba in liczby:
                if liczba % nwd != 0:
                    czy_nwd = False
                    break
            if czy_nwd:
                print("wynik = " + str(nwd))
                quit()









