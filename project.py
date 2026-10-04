import random

def main():
    print("\n Your goal is to make 10 using the given numbers.")
    print(" Use +, -, *, / and at most ONE pair of parentheses ().")
    print("Use the numbers in the same order. Type 'hint' or 'quit'.\n")

    while True:
        numbers = generate_numbers()
        print(f"Your numbers are: {' '.join(map(str, numbers))}")

        while True:
            user_input = input("Enter expression: ").strip()

            if user_input.lower() == "quit":
                print(" Thanks for playing!")
                return

            elif user_input.lower() == "hint":
                solution = find_solution(numbers)
                if solution:
                    print(f" Solution is: {solution} = 10")
                else:
                    print(" No solution possible with these numbers.")
                print(" Generating new numbers...\n")
                break  # Break to outer loop to generate new numbers

            elif not is_valid_expression(user_input, numbers):
                print("️ Invalid expression. Use digits in order and at most one set of parentheses.")
                continue

            result = evaluate_expression(user_input)
            if result is None:
                print("Invalid math (maybe division by zero?). Try again.")
            elif abs(result - 10) < 1e-6:
                print(" Correct! That makes 10!\n")
                break  # Correct answer, move to next numbers
            else:
                print(f"That equals {result}, not 10. Try again.")


def generate_numbers():
    return [random.randint(0, 9) for _ in range(4)]

def evaluate_expression(expr):
    try:
        return eval(expr)
    except ZeroDivisionError:
        return None
    except Exception:
        return None

def is_valid_expression(expr, numbers):
    digits_in_expr = [int(ch) for ch in expr if ch.isdigit()]
    if digits_in_expr != numbers:
        return False
    if expr.count('(') > 1 or expr.count(')') > 1:
        return False
    return True

def find_solution(numbers):
    ops = ['+', '-', '*', '/']

    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                expr = f"{numbers[0]}{op1}{numbers[1]}{op2}{numbers[2]}{op3}{numbers[3]}"
                if abs(evaluate_expression(expr) - 10) < 1e-6:
                    return expr

                # Add variations with one pair of parentheses
                variations = [
                    f"({numbers[0]}{op1}{numbers[1]}){op2}{numbers[2]}{op3}{numbers[3]}",
                    f"{numbers[0]}{op1}({numbers[1]}{op2}{numbers[2]}){op3}{numbers[3]}",
                    f"{numbers[0]}{op1}{numbers[1]}{op2}({numbers[2]}{op3}{numbers[3]})",
                    f"({numbers[0]}{op1}{numbers[1]}{op2}{numbers[2]}){op3}{numbers[3]}",
                    f"{numbers[0]}{op1}({numbers[1]}{op2}{numbers[2]}{op3}{numbers[3]})",
                    f"({numbers[0]}{op1}{numbers[1]}){op2}({numbers[2]}{op3}{numbers[3]})"
                ]

                for var in variations:
                    if evaluate_expression(var) is not None and abs(evaluate_expression(var) - 10) < 1e-6:
                        return var
    return None

if __name__ == "__main__":
    main()
