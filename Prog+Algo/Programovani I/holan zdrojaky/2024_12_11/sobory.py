f = open("sobory.py", "r")
print("############### "
      "CTU SOUBOR: soubor.py "
      "####################")
for radek in f:
    print( radek[:-1] )
print("############### "
      "KONCIM CETBU SOUBORU: "
      "soubor.py ##########")
f.close()

g = open("SOUBOR(VytvorenoProgramem).txt", "w")
for i in range(10_000):
    g.write(f"{i}\n")
g.close()