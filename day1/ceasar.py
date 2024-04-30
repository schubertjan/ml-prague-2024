from colorama import Fore, init

def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # check if character is an alphabet
            ascii_offset = ord('a') if char.islower() else ord('A')
            cipher_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext

# Initialize colorama for colored text
init()

def caesar_decrypt(ciphertext):
    """
    Decrypts a message encrypted using the Caesar cipher.
    Automatically detects the shift value.
    :param ciphertext: The encrypted message (ciphertext)
    :return: The decrypted plaintext
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet

    # Calculate letter frequencies in the ciphertext
    letter_counts = {letter: 0 for letter in alphabet}
    total_letters = 0

    for char in ciphertext.lower():
        if char in alphabet:
            letter_counts[char] += 1
            total_letters += 1

    # Find the most frequent letter (usually 'e' in English)
    most_frequent_letter = max(letter_counts, key=letter_counts.get)

    # Calculate the shift value based on the most frequent letter
    shift = (ord(most_frequent_letter) - ord('e')) % 26

    # Create a shifted version of the alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    # Apply the translation to the ciphertext
    plaintext = ciphertext.translate(table)

    return plaintext

def main():
    try:
        # Get user input: ciphertext
        ciphertext = input("Enter the encrypted message (ciphertext): ")

        # Decrypt the message
        plaintext = caesar_decrypt(ciphertext)

        # Print the decrypted plaintext
        print(Fore.GREEN + "Decrypted message (plaintext):", plaintext)
    except ValueError:
        print(Fore.RED + "Error: Please enter a valid ciphertext.")


def caesar_brute_force(ciphertext):
    """
    Brute-force attack to find the shift value for a Caesar cipher.
    :param ciphertext: The encrypted message (ciphertext)
    :return: A list of possible plaintexts for each shift value
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # Define the alphabet
    possible_plaintexts = []

    for shift in range(26):
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        plaintext = ciphertext.translate(table)
        possible_plaintexts.append(plaintext)

    return possible_plaintexts

# Example usage:
encrypted_message = "Qlaxv fp Qrbpaxv"
possible_messages = caesar_brute_force(encrypted_message.lower())

for shift, message in enumerate(possible_messages):
    print(f"Shift {shift}: {message}")

if __name__ == "__main__":
    main()