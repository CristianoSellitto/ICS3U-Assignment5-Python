#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that counts the number of positive numbers, negative numbers, and zeros the user inputs


def main():
    # Counts the number of positive numbers, negative numbers, and zeros the user inputs

    number_of_positives = 0
    number_of_negatives = 0
    number_of_zeros = 0
    try:
        while True:
            chosen_text = input("\nEnter a number from 0 to 9 (input 'stop' to end): ")
            if chosen_text == "stop":
                final_text = "\nYou entered "
                if number_of_positives == 1:
                    final_text = final_text + "1 positive, "
                else:
                    final_text = final_text + "{} positives, ".format(
                        number_of_positives
                    )
                if number_of_negatives == 1:
                    final_text = final_text + "1 negative, "
                else:
                    final_text = final_text + "{} negatives, ".format(
                        number_of_negatives
                    )
                if number_of_zeros == 1:
                    final_text = final_text + "and 1 zero."
                else:
                    final_text = final_text + "and {} zeros.".format(number_of_zeros)
                print(final_text)
                break
            else:
                chosen_number = float(chosen_text)
                if chosen_number > 0:
                    number_of_positives = number_of_positives + 1
                elif chosen_number < 0:
                    number_of_negatives = number_of_negatives + 1
                else:
                    number_of_zeros = number_of_zeros + 1
    except ValueError:
        print("\n{} isn't a number.".format(chosen_text))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
