from data import nevek, betegsegek
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
    print('5 - Betegség módosítása')
    print('6 - Legkevesebb ideig bent lévő beteg')
    return input('Választás: ')

def fajlBetoltes():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        darabolt=row.strip().split(';')
        nevek.append(darabolt[0])
        betegsegek.append(darabolt[1])
    file.close()


#1
def BetegekKiir():
    system('cls')
    print('~Betegek;')
    for i in range(len(nevek)):
        print(f'\t{nevek[i]}')
    input()

#2
def Teljes():
    print('~Betegek;')
    for i in range(len(nevek)):
        print(f'\t{nevek[i]} - {betegsegek[i]}')

#3
def ujBeteg():
    print('Új beteg felvétele')
    nev=input('Kérem a beteg nevét: ')
    nevek.append(nev)
    betegseg=input('Kérem a betegségét: ')
    betegsegek.append(betegseg)
    input('A beteg sikeresen felvételre került...')

#4
def kereses(keresett):
    for index,ertek in enumerate(nevek):
        if keresett == ertek:
            return index
    return -1

def Torles():
    nevek.clear()
    betegsegek.clear()
    fajlBetoltes()
    system('cls')
    print('~Beteg törlése;')
    torlendo = input('Törlendő beteg neve: ')

    if kereses(torlendo) != -1:
        nevek.remove(nevek[kereses(torlendo)])
        betegsegek.remove(betegsegek[kereses(torlendo)])
        saveFullFile()
        print('Sikeres törlés!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')
    else:
        print('Nincs ilyen beteg!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')



def Save(nevek, betegsegek):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nevek};{betegsegek}')
    file.close()


def saveFullFile():
    file = open(fajlnev, 'w', encoding = 'utf-8')
    for i in range(len(nevek)):
        file.write(f'{nevek[i]};{betegsegek[i]}')
        if (i != len(nevek) -1):
            file.write('\n')
    file.close()

#5
def BetegsegModositas():
    nevek.clear()
    betegsegek.clear()
    fajlBetoltes()
    system('cls')
    print('~Betegség módosítása;')
    keresett = input('Módosítandó beteg neve: ')

    if kereses(keresett) != -1:
        print(f'Jelenlegi betegség: {betegsegek[kereses(keresett)]}')
        betegsegek[kereses(keresett)] = input('Új betegség: ')
        saveFullFile()
        print('Sikeres módosítás!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')
    else:
        print('Nincs ilyen beteg!')
        input('A továbblépéshez nyomja meg az [ENTER] billentyűt!')

#6