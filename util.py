def tah(pole, pozice, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici"

    return pole[:pozice] + symbol + pole[pozice + 1:]

def zamen_xo(retezec):
    vysledek = []
    for znak in retezec:
        if znak == 'o':
            vysledek.append('x')
        elif znak == 'x':
            vysledek.append('o')
        else:
            vysledek.append(znak)
    return ''.join(vysledek)

def vyhodnot(pole):
    if 'ooo' in pole:
        return 'o'
    if 'xxx' in pole:
        return 'x'
    if '-' not in pole:
        return '!'
    return '-'


def vymen_o(func):
    def _wrapper(pole, symbol):
        if symbol == 'x':
            return func(pole)
        else:
            return zamen_xo(func(zamen_xo(pole)))
    return _wrapper

def vymen_x(func):
    def _wrapper(pole, symbol):
        if symbol == 'o':
            return func(pole)
        else:
            return zamen_xo(func(zamen_xo(pole)))
    return _wrapper
