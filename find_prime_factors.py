# This is a simple code to find the Prime Factors

# This function will ask the user to input an integer to find the prime factors
def find_prime_factors(): # you can specify the "number variable ()" here and call the function with a number in ()
    print("This code will find the Prime Factors of a Number!")
    print("\n### USE ONLY NUMBERS ###\n")
    # I chose this because it is easier to ask the user for the input
    number = int(input("Please enter the number you want to find its Prime Factors: "))
    # this will create an empty list to append to it
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    print(factors)


def main():
    find_prime_factors()


if __name__ == "__main__":
    main()
