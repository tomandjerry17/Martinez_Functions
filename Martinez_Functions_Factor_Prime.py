def smallestFactor():
    try:
        # Get user input for an integer
        num = int(input("\tEnter an integer >=2\n\t(Greater than or equal to 2)\n\t>> "))

        # Check if the input is greater than or equal to 2
        if num >= 2:
            smallestFactor = 0  # Initialize variable to store the smallest factor

            # Iterate through potential factors starting from 2 up to the square root of the number
            for i in range(2, int(num ** 0.5) + 1):

                if num % i == 0:
                    smallestFactor = i
                    break

            # Check if a factor was found
            if smallestFactor != 0:
                print("\tThe smallest factor other than 1 for", num, "is", smallestFactor)
            else:
                print("\t", num, "is a prime number.")
        else:
            print("\tInvalid input. Enter a number greater than 2.")

    except ValueError:
        print("\tInvalid input. Please enter a valid integer.")

    print("\n")


def prime():
    startNum = int(input("\tEnter a number [start]: "))

    # Check if the user wants to terminate the program
    if startNum == 0:
        print("\n\tProgram terminated.")

    endNum = int(input("\tEnter a number [end]  : "))

    # Check for non-negative input
    if startNum < 0:
        print("\n\tEnter a non-negative number!!\n")
    # Check if endNum is greater than or equal to startNum
    elif endNum < startNum:
        print(f"\n\tEnter a number in [end] greater than or equal to {startNum}\n")
    else:
        print(f"\n\tPrime numbers between {startNum} and {endNum} are:")

        # Loop through the range and check for prime numbers
        for x in range(startNum, endNum + 1):
            is_prime = True  # Assume x is prime unless proven otherwise

            # Check for factors
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break

            # Print x if it is prime
            if is_prime and x > 1:
                print(x, end=' ')

        print("\n\n")


def main():
    while True:
        try:
            print("Press [1] for Smallest Factor of n")
            print("Press [2] for Prime Numbers of Range")
            print("Press [3] To Stop")
            select = int(input("\n\t>> "))
            print()
            if select == 1:
                smallestFactor()
            elif select == 2:
                prime()
            elif select == 3:
                break
            else:
                print("Pick only [1] or [2] or [3]\n\n")
                continue
        except ValueError:
            print("Pick only [1] or [2] or [3]\n\n")
            continue


main()
