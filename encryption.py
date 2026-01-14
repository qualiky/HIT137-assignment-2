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
                if 'a' <= char <= 'm':
                    number = ord(char) - ord('a') + (shift1 * shift2)
                    newline += chr((number % 13) + ord('a'))
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

# Read the encrypted file
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






