from data import nevek, betegségek
from os import system
fajlnev='data.csv'

def menu():
    system('cls')
    print('~~~~~MENÜ~~~~~')
    print('0 - Kilépés')
    print('1 - Betegek nevei')
    print('2 - Betegségük')
    print('3 - Új beteg felvétele')
    print('4 - Beteg törlése')
    print('5 - Leghosszebb ideig bent lévő beteg')
    print('6 - Legkevesebb ideig bent lévő beteg')
    return input('Választás: ')

def fajlBetoltes():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        nevek.append(darabolt[0])
        betegségek.append(darabolt[1])
