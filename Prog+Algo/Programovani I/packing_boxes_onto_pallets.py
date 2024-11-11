tabulka = \
{ # kolik se vejde boxu velikosti 20 (kdyz nejdriv pouziju boxy 40) a 40 k i boxum velikosti 60
    0: (0, 0),
    1: (37, 19),
    2: (42, 15),
    3: (47, 11),
    4: (36, 9),
    5: (41, 5),
    6: (30, 3),
    7: (19, 1)
}


boxy_20, boxy_40, boxy_60, boxy_80, boxy_100, boxy_120,   = [int(n) for n in input().split()]

palety = boxy_80 + boxy_100 + boxy_120   # boxy 120, 100, 80 potrebuji kazdy vlastni paletu

palety += boxy_60 // 8  # pocet palet zcela zaplnenych jen boxy velikosti 60
boxy_60 %= 8
if boxy_60 > 0:
    palety += 1


misto_pro_20 = 91 * boxy_100 + tabulka[boxy_60][0]
misto_pro_40 = 19 * boxy_80 + tabulka[boxy_60][1]


if boxy_40 >= misto_pro_40:  # vsechna volna mista pro boxy_40 se zaplni a nejake boxy_20 zbydou
    boxy_40 -= misto_pro_40
else:                        # nebo zabalime vsechny boxy_40 a zbytek volneho mista uvolnime pro boxy_20
    nove_misto_pro_20 = (misto_pro_40 - boxy_40) * 8
    boxy_40 = 0
    misto_pro_20 += nove_misto_pro_20

if boxy_20 >= misto_pro_20:  # vsechna volna mista pro boxy_20 se zaplni a nejake boxy_20 zbydou
    boxy_20 -= misto_pro_20
else:                        # nebo zabalime vsechny boxy_20
    boxy_20 = 0

# zbyvajici boxy 20 a 40 uz muzeme prevest na boxy 20, box40 se sestava z 8 boxu velikosti 20
zbytek_k_zabaleni_20 = boxy_40 * 8 + boxy_20
palety += zbytek_k_zabaleni_20 // (120//20)**3  # kolik boxu 20 se vejde na 1 paletu

if zbytek_k_zabaleni_20 % (120//20)**3 > 0:     # nejake boxy jeste prebyly, dame je na finalni paketu
    palety += 1

print(palety)