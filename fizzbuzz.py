def main():
    userInput = getUserInput("Please enter an integer greater than 0: ")
    fizzBuzz(userInput)

def getUserInput(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                break
        # If n is not an integer, or an integer less than 1, reprompt the user.
        except ValueError:
            pass
    return n

def fizzBuzz(n):
    # Loop from 1 to the user's number.
    for _ in range(n):
        # Make _ start at 1 instead of 0.
        _ += 1
        # If the user's number is a multiple of both 3 and 5, print FizzBuzz.
        if _ % 3 == 0 and _ % 5 == 0:
            print("FizzBuzz")
        # If the user's number is a multiple of 3, print Fizz.
        elif _ % 3 == 0:
            print("Fizz")
        # If the user's number is a multiple of 5, print Buzz.
        elif _ % 5 == 0:
            print("Buzz")
        # Otherwise, print the current number.
        else:
            print(_)

if __name__ == "__main__":
    main()