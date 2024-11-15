class Ctecka:
    def precti_slovo(self):
        pass


KONEC = "konec_cteni"


class CteckaPoRadkach:
    def precti_slovo(self):
        return input("Zadej slovo:")


class CteckaZeStringu:
    def __init__(self, string):
        self.zbytek = string.split()

    def precti_slovo(self):
        if self.zbytek == []:
            return KONEC
        return self.zbytek.pop(0)


class CteckaZeSouboru:
    def __init__(self, jmeno):
        self.soubor = open(jmeno, 'r', encoding="utf-8")
        self.zbytek = []

    def precti_slovo(self):
        while self.zbytek == []:
            radka = self.soubor.readline()
            if radka == "":  # eof!
                self.soubor.close()
                print("Zaviram soubor")
                return KONEC

            self.zbytek = radka.split()
        return self.zbytek.pop(0)


class Ctecka_Filtr_JenomVelka:
    def __init__(self, ctecka):
        self.ctecka = ctecka

    def precti_slovo(self):
        slovo = self.ctecka.precti_slovo()
        while (slovo != KONEC) and (slovo != slovo.upper()):
            slovo = self.ctecka.precti_slovo()
        return slovo


class Ctecka_Filtr_MinimalniDelka:
    def __init__(self, ctecka, mindelka):
        self.ctecka = ctecka
        self.mindelka = mindelka

    def precti_slovo(self):
        slovo = self.ctecka.precti_slovo()
        while (slovo != KONEC) and (len(slovo) < self.mindelka):
            slovo = self.ctecka.precti_slovo()
        return slovo


# --------------------------------------
class SlovnikVDictionary:
    def __init__(self):
        self.seznam = dict()

    def zapocitej_slovo(self, slovo):
        if slovo not in self.seznam:
            self.seznam[slovo] = 0
        self.seznam[slovo] += 1

    def vrat_nejcastejsi_slova(self, pocet):
        vystup = []
        for i in range(pocet):
            nej_slovo = None
            nej_pocet = 0
            for slovo in self.seznam:
                if self.seznam[slovo] > nej_pocet:
                    nej_slovo = slovo
                    nej_pocet = self.seznam[slovo]
            if nej_pocet > 0:
                vystup.append((nej_slovo, nej_pocet))
                self.seznam[nej_slovo] = -self.seznam[nej_slovo]
        # ...zase obnovit...
        return vystup


# --------------------------------------------
class TiskarnaNaKonzoli:
    def __init__(self):
        pass

    def vytiskni_polozku(self, slovo, pocet):
        print(f"{pocet:5d} {slovo}")

    def vytiskni_seznam(self, seznam):
        print("---------------------")
        print("pocet slovo")
        print("---------------------")
        for polozka in seznam:
            self.vytiskni_polozku(polozka[0], polozka[1])
        print("---------------------")


import webbrowser
from datetime import datetime


class TiskarnaDoHTML:
    def __init__(self):
        pass

    def vytiskni_polozku(self, slovo, pocet):
        self.file.write(f"<tr><td>{pocet}</td><td>{slovo}</td></tr>\n")

    def vytiskni_seznam(self, seznam):
        url = datetime.now().strftime("%y%m%d_%H%M%S") + ".html"
        self.file = open(url, 'w', encoding='utf-8')
        self.file.write("<html><body><table border=1>\n")
        for polozka in seznam:
            self.vytiskni_polozku(polozka[1], polozka[0])
        self.file.write("</table>")
        self.file.close()
        webbrowser.open_new_tab(url)


##############################################

# ctecka = CteckaPoRadkach()
# ctecka = CteckaZeStringu("a b c de s a c c c d d c d e d c c c c c f d s d e d b e konec" )
# ctecka = CteckaZeSouboru("romeo-and-juliet_TXT_FolgerShakespeare.txt")
ctecka = Ctecka_Filtr_MinimalniDelka(
    Ctecka_Filtr_JenomVelka(
        CteckaZeSouboru("romeo-and-juliet_TXT_FolgerShakespeare.txt")
    ), 4)

slovnik = SlovnikVDictionary()
tiskarna = TiskarnaNaKonzoli()


# tiskarna = TiskarnaDoHTML()

# --------------------------------
def PocetSlov(ctecka, slovnik, tiskarna):
    while (slovo := ctecka.precti_slovo()) != KONEC:
        slovnik.zapocitej_slovo(slovo)

    nejcastejsi_slova = slovnik.vrat_nejcastejsi_slova(50)
    tiskarna.vytiskni_seznam(nejcastejsi_slova)


def Dialogy(pocet, ctecka, slovnik, tiskarna):
    prvni = ctecka.precti_slovo()
    druhy = ctecka.precti_slovo()
    delka = 2
    maxdelka = 1
    maxdvojice = "..."
    while (dalsi := ctecka.precti_slovo()) != KONEC:
        if dalsi != prvni:  # konec dialogu
            # vytisknout dosavadni dialog
            # print(f"{delka=} {prvni=} {druhy=}")
            dvojice = tuple(sorted([prvni, druhy]))
            slovnik.zapocitej_slovo(dvojice)
            if delka > maxdelka:
                maxdelka = delka
                maxdvojice = (prvni, druhy)
            delka = 2
        else:
            delka += 1
        prvni, druhy = druhy, dalsi
    print(f"Nejdelsi dialog: {maxdelka=} {maxdvojice=}")
    nejcastejsi_slova = slovnik.vrat_nejcastejsi_slova(pocet)
    tiskarna.vytiskni_seznam(nejcastejsi_slova)


PocetSlov(ctecka, slovnik, tiskarna)

# Dialogy(50, ctecka, slovnik, tiskarna)