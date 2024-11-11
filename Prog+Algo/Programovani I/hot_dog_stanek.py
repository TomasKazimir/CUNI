from random import randint

input_data = [randint(1, 5000) for _ in range(20_000)]
# try:
#     while (line := input()) != "":
#         input_data += [int(x) for x in line.split()]
# except: pass

max_profit = 0
best_price = 0
for i, price in enumerate(sorted(input_data, reverse=True)):
    profit = (i+1) * price
    if profit >= max_profit:
        max_profit = profit
        best_price = price

print(best_price)