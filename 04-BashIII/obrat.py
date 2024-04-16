# ve složce ./bin


! /usr/bin/python3

import sys
import os

obracena_pismena = {
    'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
    'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
    'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
    'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': 'B',
    'C': 'Ɔ', 'D': 'D', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I',
    'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ',
    'Q': 'Q', 'R': 'R', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ', 'W': 'M',
    'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ',
    '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', ',': "'",
    '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '`': ',', '(': ')',
    ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<',
    '&': '⅋', '_': '‾',
}

def obrat(text):
    return ''.join(obracena_pismena.get(c, c) for c in reversed(text))


#for line in sys.stdin:
#print(obrat(line.rstrip()))

#sys.argv

if "-" in opts:
    for line in sys.stdin:
       print(obrat(line.rstrip()))

if sys.argv == '-':
    for line in sys.stdin:
        print(obrat(line.rstrip()))


if len(sys.argv) > 1:
    for jmeno in sys.argv[1:]:
        if jmeno == '-':
            for line in sys.stdin:
                print(obrat(line.rstrip()))
        try:
            with open(jmeno,"r") as file:
                obsah = file.read()
                #for line in obsah:
                slova = obsah.split()
                for slovo in slova:
                    print(obrat(slovo))
        except FileNotFoundError:
            print(f"File not found")
else:
    for line in sys.stdin:
        print(obrat(line.rstrip()))


#opts = [opt for opt in sys.argv[1:] if opt.startswith('-')]
#args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]


                                            