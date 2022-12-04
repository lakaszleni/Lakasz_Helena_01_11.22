from functions import menu, fajlBetoltes, BetegekKiir, Teljes, ujBeteg, Torles, legkevesebbido, BetegsegModositas
from os import system
from data import nevek


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
        Torles()
    elif valasztas == '5':
        BetegsegModositas()
    elif valasztas == '6':
        system('cls')
        print("~Legkevesebb ideig bent lévő beteg; ")
        legkevesebbido()
        print(nevek[legkevesebbido()])
        input()