#Calculator
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = input(
    "Select the operation:\n"
    "A) Addition\n"
    "B) Subtraction\n"
    "C) Multiplication\n"
    "D) Division\n"
    "E) Power (applied to the first number)\n"
    "Enter your choice: "
).lower()

if c == "A" or c=="a":
    print(a + b)
elif c == "B" or c=="b":
    print(a - b)
elif c == "C" or c=="c":
    print(a * b)
elif c == "D" or c=="d":
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print(a / b)
elif c == "E" or c=="e":
    print(a ** b)
else:
    print("Invalid option.")


    
    
    

