# Homework - Lecture 11
# The input file is calls "river.txt" - a poem by Poe

# Creating a CLI with argparse
import argparse

parser = argparse.ArgumentParser(description="Text Encryption") 
parser.add_argument("--caesar", action="store_true", help="If you want to encrypt the code with Caesar's cipher write True. The default is encryption off.")
parser.add_argument("--shift", type=int, help="The # of letter you want to shift your alphabet. Enter an integer number between 1 and 25.")

# Parse command line arguments
args = parser.parse_args()

# Open & read the input file & encrypt it with caesar's cipher
def cipher(caesar=False, shift=0):
    """ This function takes an input file changes it to capital letters and - if the user in the CLI
    decides so also encrypts the text according to Caesar's cipher. The number of sifts for this cipher is given
    as command line input by the user."""
    input_filename = "river.txt"
    output_filename = "encrypted_river.txt"

    with open(input_filename, encoding="utf-8") as input_file:
        content = input_file.read()   
        content = content.upper()

        if caesar is True:
            result = ""
            for char in content:
                if char.isalpha():
                     """ This makes sure that we only transform characters"""
                     char_code = ord(char)
                     '''This gets the American Standard Code for Information Interchange - which is a number
                        that was assigned to a specific character'''
 
                     shifted_code = (char_code - ord("A") + shift) % 26 # %26 ensures that it stays within the lenght of the alphabet 
                     encrypted_char = chr(shifted_code + ord("A"))
                     result += encrypted_char
                else: result += char # this is for all non alphabetic characters to be added as well

        else:
            result = content

    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write(result)

    print(f"The encrypted file has been saved as {output_filename}.")

# Call the cipher function with parsed arguments - we did not do that in class but 
# without this the example from class also does not work for me.
cipher(args.caesar, args.shift)