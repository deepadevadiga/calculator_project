def calculate():
    print("=== Calculator ===")
    while True:
        try:
            a = float(input("First number: "))
            op = input("Operator (+ - * /): ").strip()
            b = float(input("Second number: "))
            if op == "+": result = a + b
            elif op == "-": result = a - b
            elif op == "*": result = a * b
            elif op == "/":
                if b == 0: raise ZeroDivisionError
                result = a / b
            else:
                print("Invalid operator."); continue
            print("Result:", result)
        except ValueError:
            print("Enter valid numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        if input("Again? (y/n): ").lower() != "y": break

if __name__ == "__main__":
    calculate()
