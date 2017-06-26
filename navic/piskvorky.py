from AI2 import tah_pocitace

def x_nebo_o(uzivatelsky_input):        #vybíráme si symboly
    while True:
        if symbol_hrac == 'x':
            return 'o'
        elif symbol_hrac == 'o':
            return 'x'
        else:
            continue

def vyhodnot(pole):
    """1-D piškvorky se hrají na řádku s dvaceti políčky.
    Hráči střídavě přidávají kolečka (o) a křížky (x)."""

    if 'xxx' in pole and 'ooo' in pole:
        return '!'
    elif 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

def tah(pole, cislo_policka, symbol):
  'Vrátí herní pole s daným symbolem umístěným na danou pozici'
  pole = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
  return pole


def tah_hrace(pole):
  'Zjistí, kam do pole chce hráč hrát a jestli je to možné.'
  while True:
    try:
        pozice = int(input('Prosím zadejte pozici pro další tah: '))
    except TypeError:           #pokud je pozice jiný znak, než číslo
        print('Chyba, prosím znovu zadejte číslo pozice v poli.')
    except ValueError:          #pokud pozice není celé číslo
        print('Chyba, prosím znovu zadejte číslo pozice v poli.')
    else:
        if pozice > len(pole):  #kontrola správného rozsahu pozice
            print('Pozice musí být v herním poli "0 - {0}"'.format(len(pole)-1))
        elif pozice < 0:        #kontrola kladnosti pozice
            print('Pozice musí být kladné číslo!')
        elif 'o' == pole[pozice] or 'x' == pole[pozice]:
            #kontrola obsazeni pole
            print('Pozice musí být volná!')
        else:
            return tah(pole, pozice, symbol_hrac) # vyskoc z retezce



def piskvorky1d():
    "Tvoří hrací pole a oznamuje celkový výsledek hry."
    pole = 20*'-'
    while True:
        if vyhodnot(pole) == '-':
            pole = tah_hrace(pole)
            print(pole)
            pole = tah_pocitace(pole)
            print(pole)

    if vyhodnot(pole) == symbol_hrac:
        print('Jóóó, vyhrává hráč! Gratulujeme!')
    elif vyhodnot(pole) == symbol_pc:
        print('Smůla, tentorkát vyhrál počítač. Zkus se příště víc snažit...')
    else:
        print('Remíza! Jsi stejně dobrý/á, jako naše úžasná umělá inteligence.')


print('Začínáme s polem:', 20*'-')
symbol_hrac = input('Chceš mít x nebo o?')
print('V této hře hraje hráč: ', symbol_hrac)
symbol_pc = x_nebo_o(symbol_hrac)
print('Počítač bude mít ', symbol_pc)
piskvorky1d()
