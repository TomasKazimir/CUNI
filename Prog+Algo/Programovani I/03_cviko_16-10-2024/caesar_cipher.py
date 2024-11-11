key = int(input())
message = input().strip().upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caesar = ""

for char in message:
    if char in alphabet:
        caesar += alphabet[(alphabet.index(char) + key) % len(alphabet)]
    else:
        caesar += char

print(caesar)
