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