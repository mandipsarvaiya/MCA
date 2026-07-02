# bill torrent:
n = int(input("Number of items: "))
total = 0

for i in range(n):
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    total += price * qty

print("Total Bill:", total)

if total > 1000:
    total -= total * 0.1
    print("After 7% discount:", total)