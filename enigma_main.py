import sys


import enigma_encode
import enigma_menu
from  enigma_decode import decode


__author__ = 'Kris Armstrong'


def print_option_code(option_key):
    """
    Format and print the option code.

    Args:
    option_key (list): The option key to be formatted and printed.

    Returns:
    None: This function only prints the option code.
    """
    if not isinstance(option_key, list):
        raise TypeError("option_key must be a list.")

    # Convert the list of numbers into a continuous string
    continuous_str = ''.join(map(str, option_key))

    # Split the continuous string into chunks of 4 characters
    chunk_size = 4
    chunks = [continuous_str[i:i + chunk_size] for i in range(0, len(continuous_str), chunk_size)]

    # Join the chunks with spaces
    formatted_code = ' '.join(chunks)

    print("Option Code:", formatted_code)


def ask_to_continue():
    """
    Asks the user whether they want to generate another option code.
    Continues or exits the program based on the user's response.
    """
    while True:
        answer = input("Would you like to generate another Option Code (Y/N): ").lower()
        if answer.startswith("y"):
            main()
            break
        elif answer.startswith("n"):
            print("OK, goodbye! :-)")
            sys.exit(0)
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


def main():
    """
    Main function for the Enigma V3.5 program.
    Allows the user to encode or decode messages using the Enigma machine.
    """
    print("Enigma V3.5")

    while True:
        choice = input("Do you want to (E)ncode or (D)ecode? Enter E or D: ").upper()
        if choice == 'E':
            while True:
                serial_number = input("Enter your 7 digit serial Number: ")
                if len(serial_number) == 7 and serial_number.isdigit():
                    product_code, option_code = enigma_menu.product_code_menu()

                    temp_check_sum = '00'
                    in_string = temp_check_sum + product_code + serial_number + option_code

                    # Calculating Checksum
                    modified_key_code = enigma_encode.encode_checksum_calc(in_string)

                    # Calculating Option Key
                    option_key = (enigma_encode.encode_option_code_calc
                                  (modified_key_code))

                    # Printing the Option Code
                    print_option_code(option_key)  # Ensure this function is defined

                    # Generation More option codes?
                    ask_to_continue()  # Ensure this function is defined
                    break
                else:
                    print(f"You entered {len(serial_number)} digits. Please enter exactly 7 digits.")

        elif choice == 'D':
            # Get the encoded option code from the user
            encoded_option_code = input("Enter the option code to decode: ")

            # Call the decode function
            decoded_data, original_key = decode(encoded_option_code)

            # Check if the decode function returned valid data
            if decoded_data is None or original_key is None:
                print("Decoding failed.")
            else:
                # Print the decoded data and the original key
                print("Decoded Data:", decoded_data)
                print("Original Key:", original_key)

            # Ask to decode another code or exit
            ask_to_continue()

        else:
            print("Invalid choice. Please enter E to encode or D to decode.")


if __name__ == "__main__":
    main()
