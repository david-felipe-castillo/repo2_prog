def encode(number):
    number_str = str(number)
    encoded_number = ''
    for char in number_str:
        # Convert the character to an integer, add 3 to it, and convert it back to a string
        encoded_digit = str(int(char) + 3)
        # Append the encoded digit to the encoded number string
        encoded_number += encoded_digit
    return int(encoded_number)

# def decode(encoded_number):
#     encoded_str = str(encoded_number)
#     decoded_number = ''
#     for char in encoded_str:
#         # Convert the character to an integer, subtract 3 from it, and convert it back to a string
#         decoded_digit = str(int(char) - 3)
#         # Append the decoded digit to the decoded number string
#         decoded_number += decoded_digit
#     return int(decoded_number)

def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Enter an choice: ")

        if choice == "1":
            number = int(input("Please enter your password to encode: "))
            encoded_number = encode(number)
            print("Your password has been encoded and stored!")
        # elif choice == "2":
        #     decoded_number = decode(encoded_number)
        #     print(f"The encoded password is {decoded_number}, and the original password is {encoded_number}.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

main()