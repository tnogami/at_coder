N = int(input())
hexa = hex(N)[2:]
hexa = hexa.upper()
if len(hexa) == 1:
    hexa = "0"+hexa
print(hexa)