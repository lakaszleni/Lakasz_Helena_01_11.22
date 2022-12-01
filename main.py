from functions import menu, fajlBetoltes, BetegekKiir, Teljes, ujBeteg
from os import system

fajlBetoltes()

valasztas = ''

while valasztas !='0':
    valasztas = menu()
    if valasztas == '1':
        BetegekKiir()
    elif valasztas == '2':
        system('cls')
        Teljes()
        input('...')
    elif valasztas == '3':
        ujBeteg()
    elif valasztas == '4':
        pass
    elif valasztas == '5':
        pass
    elif valasztas == '6':
        pass