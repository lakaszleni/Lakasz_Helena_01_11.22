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
    print('5 - Leghosszebb ideig bent lévő beteg')
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

def eredmenyMenteseFájlVégére(nev,betegsegek):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};{betegsegek}')
    file.close()


#4
def betegTorlese():
    system('cls')
    print('~Beteg törlése; ')
    BetegekKiir()
    sSz=int(input('\nKit töröljünk?: '))
    nevek.pop(sSz-1)
    betegsegek.pop(sSz-1)
    mentesFajlba()
    input('Sikeres törlés.')

def mentesFajlba():
    file=open(fajlnev,'w',encoding='utf-8')
    for i in range(len(nevek)):
        if i>0:
            file.write('\n')
        file.write(f'{nevek[i]};{betegsegek[i]}')
    file.close()