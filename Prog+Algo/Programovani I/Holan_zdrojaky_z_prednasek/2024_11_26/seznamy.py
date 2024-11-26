class SeznamDvojic_VListu:
    def __init__(self):
        self.seznam = []

    def pridej_dvojici(self, dvojice):
        self.seznam.append(dvojice)

    def najdi_sousedy(self, prvek):
        vys = []
        for a, b in self.seznam:
            if a == prvek:
                vys.append(b)
            elif b == prvek:
                vys.append(a)
        return vys


class Seznam_VListu:
    def __init__(self):
        self.seznam = []

    def obsahuje(self, prvek):
        return prvek in self.seznam

    def pridej(self, prvek):
        self.seznam.append(prvek)

    def vyber(self):
        if len(self.seznam) == 0:
            return None
        return self.seznam.pop()


class Fronta_VListu(Seznam_VListu):
    def vyber(self):
        if len(self.seznam) == 0:
            return None
        return self.seznam.pop(0)
