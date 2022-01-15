#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 12, 2021
# This program checks the condition at the end of the loop.
def main():
    # factorial loop
    loop_counter = 0
    factorial_answer = 1

    # get user number
    user_number = int(input("Enter a whole number: "))
    print("")

    # calculate the user number and factorial answer
    while True:
        loop_counter = loop_counter + 1
        factorial_answer = factorial_answer * loop_counter
        print("Tracking {} times through loop.".format(loop_counter))
        if loop_counter >= user_number:
            break

        print("")
        print("{}! = {}".format(user_number, factorial_answer))


if __name__ == "__main__":
    main()
