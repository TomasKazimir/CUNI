n = int(input())

out = ""
while n > 0:
    out += str(divmod(n, 2)[1])
    n = divmod(n, 2)[0]
if out == "":
    out = "0"
print(out[::-1])
