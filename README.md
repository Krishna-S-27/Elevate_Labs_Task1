# Calculator CLI App

A simple and interactive **Command Line Interface (CLI)** calculator written in Python. This app allows you to perform basic arithmetic operations like addition, subtraction, multiplication, division, remainder, and exponentiation on multiple numbers entered by the user.
<p align="center">
  <img src="https://img.shields.io/badge/python-3.6%2B-blue?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License" />
  <img src="https://img.shields.io/github/forks/Krishna-S-27/calculator?style=social" alt="Forks" />
  <img src="https://img.shields.io/github/stars/Krishna-S-27/calculator?style=social" alt="Stars" />
</p>

---

## 🚀 Features

- ✅ Addition, Subtraction, Multiplication, Division
- ✅ Remainder and Exponentiation
- ✅ Supports multiple numbers as input
- ✅ Handles invalid inputs and errors like division/modulo by zero
- ✅ Option to repeat calculations without restarting the app

---

## 📦 Requirements

- Python 3.x

---

## 📥 Installation

1. Clone this repository:
   git clone https://github.com/Krishna-S-27/Elevate_Labs_Task1.git
2.Run the Calculator:
  python Calculator_CLI_App.py

## 💻 Usage

After running the script, you'll be prompted to:
✅ Choose an operation from the menu (1–6)
✅ Enter space-separated numbers
✅ See the calculated result
✅ Optionally, perform another calculation or exit

## 📘Methods Used (Theory)
Below is the logic used for each arithmetic operation implemented in this CLI calculator:

## 1️⃣ Addition
Method Used: Python's built-in sum() function.

Explanation: Adds all numbers in the list.

Example: 5 + 2 + 3 = 10

## 2️⃣ Subtraction
Method Used: Iterative subtraction using a loop.

Explanation: Subtracts each number from the running total.

Example: 10 - 2 - 3 = 5

## 3️⃣ Multiplication
Method Used: Loop through numbers multiplying each.

Explanation: Starts from 1 and multiplies each value.

Example: 2 * 3 * 4 = 24

## 4️⃣ Division
Method Used: Iterative division using a loop.

Explanation: Divides the current result by each next value.

Edge Case: Checks and handles division by zero.

Example: 100 / 2 / 5 = 10

## 5️⃣ Remainder (Modulus)
Method Used: Uses % operator inside a loop.

Explanation: Computes remainder sequentially.

Edge Case: Avoids division by zero.

Example: 10 % 3 = 1

## 6️⃣ Exponentiation
Method Used: Python's ** operator.

Explanation: Applies exponentiation in sequence.

Example: 2 ** 3 ** 2 = 512 (Right-to-left associativity)

## 👨‍💻 Author
Krishna Shalawadi
GitHub: @Krishna-S-27
