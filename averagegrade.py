n1 = float(input("Enter your first grade: "))

n2 = float(input("Enter your second grade: "))

m = (n1 + n2) / 2

if m >= 6:
    print("You passed! CONGRATS!!")
else:
    print("You failed. KEEP STUDYING!")
print(f"Your average grade is: {m:.1f}")



