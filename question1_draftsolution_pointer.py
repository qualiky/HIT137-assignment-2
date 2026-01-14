# GROUP NAME: SYDN22
# GROUP MEMBERS:
# Aryan Kapri: s398551
# Yasmeen Begum: s395593
# Bishesh Paudel: s397921
# Sandeep Gautam: s397880

# Create a program that reads the text file "raw_text.txt", encrypts its contents using a
# simple encryption method, and writes the encrypted text to a new file "encrypted_text.txt".
# Then create a function to decrypt the content and a function to verify the decryption was successful.
#
#
# Requirements
# The encryption should take two user inputs (shift1, shift2), and follow these rules:
# • For lowercase letters:
#   • If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * shift2 positions
#   • If the letter is in the second half (n-z): shift backward by shift1 + shift2 positions
# • For uppercase letters:
#   • If the letter is in the first half (A-M): shift backward by shift1 positions
#   • If the letter is in the second half (N-Z): shift forward by shift2² positions (shift2 squared)
# • Other characters:
#   • Spaces, tabs, newlines, special characters, and numbers remain unchanged
#
#
# Main Functions to Implement
# 1. Encryption function: Reads from "raw_text.txt" and writes encrypted content to "encrypted_text.txt".
# 2. Decryption function: Reads from "encrypted_text.txt" and writes the decrypted content to "decrypted_text.txt".
# 3. Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints whether the decryption was successful or not.
#
#
# Program Behavior
# When run, your program should automatically:
#   1. Prompt the user for shift1 and shift2 values
#   2. Encrypt the contents of "raw_text.txt"
#   3. Decrypt the encrypted file
#   4. Verify the decryption matches the original
#
# Author: Sandeep Gautam


# This is the first function that takes a file and encrypts it. In this case, we are just taking the input
def encryptContent(inputFile, outputFile, shift1, shift2):
    plainText = inputFile.read()
    cipherString = ""
    # We're appending the ciphered character to an empty string as we go. Here, we work with the ASCII character
    # codes, performing addition/
    for letter in plainText:
        if letter >= 'a' and letter <= 'm':
            cipherString += (chr((ord(letter) - ord('a') - (shift1 * shift2)) % 26 + ord('a')))
        elif letter > 'm' and letter <= 'z':
            cipherString  += (chr((ord(letter) - ord('m') - (shift1 + shift2)) % 26 + ord('m')))
        elif letter > 'A' and letter <= 'M':
            cipherString  += (chr((ord(letter) - ord('A') - (shift1)) % 26 + ord('A')))
        elif letter > 'M' and letter < 'Z':
            cipherString  += (chr((ord(letter) - ord('M') + (shift1**2)) % 26 + ord('M')))

    outputFile.write("".join(cipherString))


def decryptContent(inputFile, outputFile, shift1, shift2):
    cipherText = outputFile.read()
    plainString = ""
    for letter in cipherText:
        if letter >= 'a' and letter <= 'm':
            plainString += (chr((ord(letter) - ord('a') + (shift1 * shift2)) % 26 + ord('a')))
        elif letter > 'm' and letter <= 'z':
            plainString  += (chr((ord(letter) - ord('m') + (shift1 + shift2)) % 26 + ord('m')))
        elif letter > 'A' and letter <= 'M':
            plainString  += (chr((ord(letter) - ord('A') + (shift1)) % 26 + ord('A')))
        elif letter > 'M' and letter < 'Z':
            plainString  += (chr((ord(letter) - ord('M') - (shift1**2)) % 26 + ord('M')))

    print(plainString)

def main():
    # We open the files for input and output here, and pass the references to the file across both encryption and
    # decryption function. This keeps the reference to the file input and output in the main stack instead of
    # opening new references to the file within individual functions. It's a good practice to keep this centralised,
    # especially when working with things like FFI and direct C interface if ever needed.

    inputFile = open('raw_text.txt', '+w')
    outputFile = open('encrypted_text.txt', '+w')

    # We take the shift1 and shift2 value input from the user. Ideally, for a "stronger" encryption, we want to accept
    # any arbitrary value of shift1 and shift2 (integers), and use the modulo operator to rotate the values. This helps
    # us rotate even if the values exceed 26 (the max length of alphabet). Ideally, this should work normally, but if this
    # fails, we will fall back to another acceptable way. However, this encryption is NOT ideal for secure encryption in any way
    # and should not be used for things like password encryption

    shift1 = 0
    shift2 = 0

    while True:
        try:
            shift1 = int(input("Please enter the first shift value: "))
            if shift1 <= 0:
                print("Please enter a valid first shift number (greater than zero): ")
            else:
                break
        except ValueError:
            print("Please enter a valid first shift number (greater than zero): ")

    while True:
        try:
            shift2 = int(input("Please enter the second shift value: "))
            if shift2 <= 0:
                print("Please enter a valid second shift number (greater than zero): ")
            else:
                break
        except ValueError:
            print("Please enter a valid second shift number (greater than zero): ")

    encryptContent(inputFile, outputFile, shift1, shift2)
    decryptContent(inputFile, outputFile, shift1, shift2)


if __name__ == "__main__":
    main()
