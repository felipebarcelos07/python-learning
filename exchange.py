print("--- USD Currency Converter ---")

rate = 5.00

brl = float(input("How many BRL do you want to convert? "))

usd = brl / rate

print(f"Result: ${usd:.2f} usd")

if usd > 1000:
    print("Status: Great budget!")
else:
    print("Status: Keep saving!")
