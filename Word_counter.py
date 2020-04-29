import argparse
import sys


def main():
    prg_parser = argparse.ArgumentParser(description='Soubor.')
    prg_parser.add_argument('soubor')
    prg_parser.add_argument("znaky", help="Počítat znaky", action="store_true")
    prg_parser.add_argument("radky", help="Počítat řádky", action="store_true")
    prg_parser.add_argument("slova", help="Počítat slova", action="store_true")
    arguments = prg_parser.parse_args()
    try:
        f = open(arguments.soubor, "r")
        f = f.read()
        flag = False
        if arguments.slova:
            pocet_slov = f.count(' ') + len(f.split('\n'))
            print(f"Počet slov: {pocet_slov}")
            flag = True
        if arguments.radky:
            pocet_radku = len(f.split('\n'))
            print(f"Počet řádků: {pocet_radku}")
            flag = True
        if arguments.znaky:
            pocet_znaku = len(f)
            print(f"Počet znaků: {pocet_znaku}")
            flag = True
        if not flag:
            pocet_slov = f.count(' ') + len(f.split('\n'))
            pocet_znaku = len(f)
            pocet_radku = len(f.split('\n'))
            print(f"Počet slov: {pocet_slov}\nPočet znaků: {pocet_znaku}\nPočet řádků: {pocet_radku}")
    except:
        print("Pokazilo se to")
        sys.exit(1)
def word_counter(f):
    pocet_slov = f.count(' ') + len(f.split('\n'))
    return pocet_slov
def znaky_counter(f):
    pocet_znaku = len(f)
    return pocet_znaku
def line_counter(f):
    pocet_radku = len(f.split('\n'))
    return pocet_radku

main()