# Make 10 Game

**Note:** This repository is a public portfolio copy of my final project for Harvard CS50’s Introduction to Programming with Python. The original version was submitted through CS50’s course submission system.

#### Video Demo: https://youtu.be/vppqqNDNDrQ
#### Description:

**Make 10** is a terminal-based arithmetic game where the player is given four random single-digit numbers (between 0 and 9) and must use them — in the exact order provided — along with arithmetic operations (+, -, *, /) and at most one pair of parentheses to form an expression that evaluates to **exactly 10**.

The idea behind this project was to create a fun, fast-paced game that challenges both math skills and logical thinking, inspired by the classic "Make 24" game but simplified for a CS50P audience and the final project criteria.

---

### How It Works

When the game starts, users are welcomed and instructed on the rules. A random set of four digits is then generated and displayed. The user is expected to input a mathematical expression that:

- Uses all four digits in order
- Includes any combination of the four basic operations
- Optionally includes one set of parentheses
- Must evaluate exactly to 10

If the user inputs a correct expression that results in 10, they are congratulated, and new numbers are generated. If the input is invalid or incorrect, they are prompted to try again. The user may also type `"hint"` to get a valid solution (if one exists) or `"quit"` to exit the game.


### Files and Their Purpose

#### `project.py`
This is the main file that contains all the logic and runs the game. It includes:

- `main()` – The entry point that calls the `play_game()` function.
- `generate_numbers()` – Generates and returns a list of four random digits (0-9).
- `evaluate_expression(expr)` – Safely evaluates the given expression using `eval()` and returns the result.
- `is_valid_expression(expr, numbers)` – Ensures that the input expression uses the correct digits in the correct order, and restricts excessive parentheses.
- `find_solution(numbers)` – Attempts to generate a valid expression that evaluates to 10 using brute-force combinations of operations and parentheses.
- `play_game()` – Controls the game loop, handles input/output, hints, validation, and scoring logic.

All these functions are written at the top level of the file as required by CS50P guidelines.

#### `test_project.py`
Contains unit tests for three critical functions:

- `test_generate_numbers()` – Confirms that the output is a list of four digits.
- `test_evaluate_expression()` – Verifies correct evaluation and handles errors like division by zero.
- `test_is_valid_expression()` – Ensures that only valid expressions (correct digit order and allowed parentheses) pass.

You can run all tests using `pytest test_project.py`.

#### `requirements.txt`
Lists required dependencies:
- No external libraries are needed for this project, so the file is empty.


### Design Choices

- **Simple CLI Experience:** I chose a text-based interface to keep the project light and focus on logic and usability.
- **Expression Validation:** Instead of parsing expressions manually, I used Python’s `eval()` with controlled input and logic to minimize security and logic flaws.
- **Brute Force Solver (Hint):** The `find_solution()` function brute-forces valid expressions by trying all combinations of arithmetic operations and one pair of parentheses. While not the most efficient, it works well for the problem size.
- **User Experience:** Clear instructions, meaningful error messages, and helpful hints ensure a smooth user experience.



```bash
python project.py
