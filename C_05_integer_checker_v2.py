# functions goes here
def int_check(question, low, high):
    """"Checks that users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# loop for testing purposes...
while True:
    print()

    # ask user for integer
    my_num = int_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")
