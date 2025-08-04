def calculator():
    print()
    print("Hello Everyone!!\nWelcome To Calculator CLI App!")
    print()

    while True:
        user_input = input("What operation do you want to execute (enter 1 to 6):\n"
                           "1. Addition\n"
                           "2. Subtraction\n"
                           "3. Multiplication\n"
                           "4. Division\n"
                           "5. Remainder\n"
                           "6. Exponentiation\n")
        if user_input.isdigit():
            user = int(user_input)
            if 1 <= user <= 6:
                if user == 6:
                    print("Example: num1 = 5 and num2 = 2 then result will be num1**num2 == 5**2 == 25")
                break
            else:
                print("Please enter a number between 1 and 6.\n")
        else:
            print("You have not entered a valid number! Try again.\n")

    numbers = input("Enter numbers separated by spaces: ").split()

    try:
        nums = [float(n) for n in numbers]

        if user == 1:
            result = sum(nums)
            print(f"Result: {result}")

        elif user == 2:
            results = []
            for i in range(len(nums) - 1):
                result = nums[i] - nums[i + 1]
                results.append(result)
            print(f"Results of consecutive subtractions: {results}")
            print(f"Final result: {results[-1]}")

        elif user == 3:
            results = []
            for i in range(len(nums) - 1):
                result = nums[i] * nums[i + 1]
                results.append(result)
            print(f"Results of consecutive multiplications: {results}")
            print(f"Final result: {results[-1]}")

        elif user == 4:
            results = []
            for i in range(len(nums) - 1):
                if nums[i + 1] == 0:
                    print("Division by zero encountered.")
                    break
                result = nums[i] / nums[i + 1]
                results.append(result)
            if results:
                print(f"Results of consecutive divisions: {results}")
                print(f"Final result: {results[-1]}")

        elif user == 5:
            results = []
            for i in range(len(nums) - 1):
                if nums[i + 1] == 0:
                    print("Modulus by zero is not allowed.")
                    break
                result = nums[i] % nums[i + 1]
                results.append(result)
            if results:
                print(f"Results of consecutive remainders: {results}")
                print(f"Final result: {results[-1]}")

        elif user == 6:
            results = []
            for i in range(len(nums) - 1):
                result = nums[i] ** nums[i + 1]
                results.append(result)
            print(f"Results of consecutive exponentiations: {results}")
            print(f"Final result: {results[-1]}")

    except ValueError:
        print("Oops! Make sure all inputs are valid numbers.")


while True:
    calculator()
    again = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("\nThank you for using the Calculator CLI App!!")
        break
