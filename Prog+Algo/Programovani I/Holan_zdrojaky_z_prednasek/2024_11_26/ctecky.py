class CteckaZKonzole:
    def precti_radek(self):
        return input("Zadej radek vstupu: ")


class CteckaZeStringu:
    """
    V __init__ ulozi vstupni string do self.vstup a pri volani precti_radek() postupne vraci radek za radkem.
    """
    def __init__(self, string):
        self.vstup = string.split('\n')

    def precti_radek(self):
        assert self.vstup != [], "Všechny řádky byly již přečteny! Uz ti nemám co vrátiti :("
        return self.vstup.pop(0)
