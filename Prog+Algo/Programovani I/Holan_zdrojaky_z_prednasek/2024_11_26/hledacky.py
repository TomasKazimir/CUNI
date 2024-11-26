class Hledacka:
    def hledej(self, start, cil, dvojice, neprozkoumane, zname):
        neprozkoumane.pridej(start)
        zname.pridej(start)
        while (prvek := neprozkoumane.vyber()) != None:
            print(f"zkoumam: {prvek}")
            for s in dvojice.najdi_sousedy(prvek):
                print(f"...{s}")
                if s == cil:
                    return "*** nalezeno ***"
                if not zname.obsahuje(s):
                    zname.pridej(s)
                    neprozkoumane.pridej(s)
        return "--- nenalezeno ---"


class Hledacka_SCestou:
    # kopie tridy Hledacka, lisi se jenom v radkach oznacenych  ###
    def hledej(self, start, cil, dvojice, neprozkoumane, zname):
        neprozkoumane.pridej((start,[start]))                   ###
        zname.pridej(start)
        while (prvek_cesta := neprozkoumane.vyber()) != None:   ###
            prvek, cesta = prvek_cesta                          ###
            print(f"zkoumam: {prvek,cesta}")                    ###
            for s in dvojice.najdi_sousedy(prvek):
                print(f"...{s}")
                if s == cil:
                    return f"*** nalezeno {cesta+[cil]} ***"    ###
                if not zname.obsahuje(s):
                    zname.pridej(s)
                    neprozkoumane.pridej((s,cesta+[s]))         ###
        return "--- nenalezeno ---"
