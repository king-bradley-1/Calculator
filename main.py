def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        raise ZeroDivisionError("You are trying to divide by zero which is invalid.")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    continue_calculation = True
    fn = input("Enter the first number: ")
    try:
        fn = int(fn)
        while continue_calculation:
            op = input("Select an operation: '+' '-' '*' '/': ")
            if op not in operations.keys():
                raise ValueError("Invalid Operation.")
            sn = input("Select the second number: ")
            sn = int(sn)
            result = operations[op](fn, sn)
            print(f"The result is: {result}")
            to_continue = input("Do you wish to continue? Press 'y' for Yes or 'n' for No: ").lower()
            if to_continue not in ["y", "n"]:
                print("Invalid input. Shutting down the calculator.")
                continue_calculation = False
            else:
                fn = result
    except ValueError:
        print("Invalid input. Shutting down the calculator.")
        calculate()


if __name__ == "__main__":
    calculate()
