# Create a program that reads the text file "raw_text.txt", encrypts its contents using a simple encryption method, and writes the encrypted text to a new file"encrypted_text.txt". Then create a function to decrypt the content and a function to verify the decryption was successful.
# Requirements
# The encryption should take two user inputs (shift1, shift2), and follow these rules:
# • For lowercase letters:
#   o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * shift2 positions
#   o If the letter is in the second half (n-z): shift backward by shift1 + shift2 positions
# • For uppercase letters:
#   o If the letter is in the first half (A-M): shift backward by shift1 positions
#   o If the letter is in the second half (N-Z): shift forward by shift2² positions (shift2 squared)
# • Other characters:
#   o Spaces, tabs, newlines, special characters, and numbers remain unchanged
# Main Functions to Implement
# 1. Encryption function: Reads from "raw_text.txt" and writes encrypted content to "encrypted_text.txt" .
# 2. Decryption function: Reads from "encrypted_text.txt" and writes the decrypted content to "decrypted_text.txt" .
# 3. Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints whether the decryption was successful or not.
# Program Behavior
# When run, your program should automatically:
# 1. Prompt the user for shift1 and shift2 values
# 2. Encrypt the contents of "raw_text.txt"
# 3. Decrypt the encrypted file
# 4. Verify the decryption matches the original
# (Caesar Ciper's modification) [10]

#Accept shift 1 and Shift 2 numbers from the user for encryption
shift1 = int(input("Enter a shift1 number: "))
shift2 = int(input("Enter a shift2 number: "))

# Create an encryption file to write the encrypted content
write_encrypted_file = open("encryption_text.txt", "w")

# String to hold raw text content before encrypted and later use it to compare with decrypted content
raw_text_file_content = ""

# Read the raw_text.txt file
input_file = "raw_text.txt"
with open(input_file, "r") as file:
    try :
        for line in file:
            newline = ""
            content = ""
            for char in line:
                # First holding the original character to be later added to the "raw_text_file_content"
                content += char
                # Perform encryption operation based on the alphabets a-m, n-z, A-M and N-Z using shift1 and shift2
                #
                # ord() function takes in a unicode character and returns the ascii value. the ascii value is the number
                # on which we can operate, since these values are much more easier to perform the rotational calculation on
                # instead of counting the number of characters, in an array for example. We do the math directly instead.
                #
                # The modulo by 13 is important because we're operating on first and second half of 26 characters.
                # At the end of operation, we convert the ascii number back to character with chr().
                if 'a' <= char <= 'm':
                    number = ord(char) - ord('a') + (shift1 * shift2) # [8]
                    newline += chr((number % 13) + ord('a')) # [9]
                elif 'n' <= char <= 'z':
                    number = ord(char) - ord('n') - (shift1 + shift2)
                    newline += chr(number % 13 + ord('n'))
                elif 'A' <= char <= 'M':
                    number = ord(char) - ord('A') - shift1
                    newline += chr(number % 13 + ord('A'))
                elif 'N' <= char <= 'Z':
                    number = (ord(char) - ord('N') + (shift2 * shift2))
                    newline += chr((number % 13) + ord('N'))
                else:
                    newline += char
            # Storing the original content of the line
            raw_text_file_content += content
            # Writing to the encrypted file
            write_encrypted_file.write(newline)
    except Exception as e:
        # Catching the exception
        print(f"Error in encrypting the raw text file{e}")
    finally:
        # closing the encrypted file
        write_encrypted_file.close()

#New file to store the decrypted content
write_decrypted_file = open("decrypted_text.txt","w")

# String to store the contents after decryption
decrypted_file_content = ""

# Reading the encrypted file
encrypted_file = "encryption_text.txt"
with open("encryption_text.txt", "r") as file:
    try:
        for line in file:
            newline = ""
            for char in line:
                # Perform decrypted operation based on the alphabets a-m, n-z, A-M and N-Z using shift1 and shift2
                if 'a' <= char <= 'm':
                    number = ord(char) - ord('a') - (shift1 * shift2)
                    newline += chr((number % 13) + ord('a'))
                elif 'n' <= char <= 'z':
                    number = ord(char) - ord('n') + (shift1 + shift2)
                    newline += chr(number % 13 + ord('n'))
                elif 'A' <= char <= 'M':
                    number = ord(char) - ord('A') + shift1
                    newline += chr(number % 13 + ord('A'))
                elif 'N' <= char <= 'Z':
                    number = ord(char) - ord('N') - (shift2 * shift2)
                    newline += chr(number % 13 + ord('N'))
                else:
                    newline += char
            # Storing the decrypted file content
            decrypted_file_content += newline
            # Writing to the decrypted file
            write_decrypted_file.write(newline)
    except Exception as e:
        # Catching the exception
        print(f"Error in decrypting the encrypted file{e}")
    finally:
        # Closing the decrypted file
        write_decrypted_file.close()

# Comparing the raw text file content with decrypted file content
if raw_text_file_content==decrypted_file_content:
    print("Decrypted text matches the original text")
else:
    print("Decrypted text does not match the original text")
