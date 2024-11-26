def nacti_vstup(ctecka, dvojice):
    """
    Vstup má tvar:
    - řádky obsahující dvojice
    - prázdný řádek
    - dvojice start a cíl
    """

    while (radek := ctecka.precti_radek()) != "":
        dvojice.pridej_dvojici(radek.split())
    # ted jsme precetl prazdny radek => jeste nacist start a cil:
    return ctecka.precti_radek().split()


def proved_vypocet(hledacka, start, cil, dvojice, neprozkoumane, zname):
    return hledacka.hledej(start, cil, dvojice, neprozkoumane, zname)


def vytiskni_vysledek(tiskarna, vysledek):
    tiskarna.vytiskni("========================")
    tiskarna.vytiskni(vysledek)
    tiskarna.vytiskni("========================")


################
import ctecky
import hledacky
import seznamy
import tiskarny

# ctecka = ctecky.CteckaZKonzole()
ctecka = ctecky.CteckaZeStringu(
"""1 2
1 3
2 5
3 8
2 8
2 9
8 6
6 7
7 18
9 18

1 9""")

dvojice = seznamy.SeznamDvojic_VListu()
zname = seznamy.Seznam_VListu()

# neprozkoumane = seznamy.Seznam_VListu()  # zasobnik - do hloubky
neprozkoumane = seznamy.Fronta_VListu()   # fronta - do sirky

# hledacka = hledacky.Hledacka()
hledacka = hledacky.Hledacka_SCestou()

tiskarna = tiskarny.Tiskarna_NaKonzoli()

# ---------------------------------------
start, cil = nacti_vstup(ctecka, dvojice)
vys = proved_vypocet(hledacka, start, cil, dvojice, neprozkoumane, zname)
vytiskni_vysledek(tiskarna, vys)
