text = ""
try:
    while (line := input()) != "":
        text += line + " "
except:
    pass 
for line in text.split(".")[:-1]:
    print(line.strip() + ".")