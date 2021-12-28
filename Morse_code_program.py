
#This is the morse dictionary which contains the English alphabet and corresponding morse code.
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/',
         '': ' '}

def function_encode(encode_msg):
    # function for encode
    # makes variable "morse_code" which is empty string
    morse_code = " "
    # for loop for letter in encode.msg
    for letter in encode_msg:
        # if letter is not equal to empty string
        if letter != ' ':
            # add morse[letter and add empty string]
            morse_code += morse[letter] + ' '
            # provide the morse for each letter in range
    print("------------------------------")
    print("   Encrypted message below")
    print(morse_code)
    print("------------------------------")


def function_decode(decode_msg):
    # a extra space in added to decode_msg to allow the program to access the last morse code
    decode_msg += ' '
    eng_msg = ''
    citext = ''
    i = 0
    for letter in decode_msg:
        # checks for space
        if (letter != ' '):
            # This counter is to keep track of spaces
            i = 0
            # Store morse code of a single alphabet character
            citext += letter
            # If there is a space
        else:
            # This counter equals the spaces between letters
            # If there is one space that means a space between letters
            i += 1
            # This counter represents the spaces between words
            # If there are two spaces that indicates a new word.
            if i == 2:
                # Adding space between two words
                eng_msg += ' '
            else:
                # Accessing the morse code dictionary keys by use of values to decode the morse code.
                eng_msg += list(morse.keys())[list(morse.values()).index(citext)]
                citext = ''
    print("------------------------------")
    print("   Decrypted message below")
    print(eng_msg)
    print("------------------------------")


# This "system_on" variable is set to the True Boolean
# "system_on" starts the program and keeps it operating
system_on = True

# This is the display of my program
print("********************************")
print("*** Welcome to morse_code.py ***")
print("********************************\n")
print("Would you like to encode english to morse code?\nHow about decode morse code into english?")

# This is a while loop that for as long as system_on
# is set to True it will continually ask you for the user's input
while system_on == True:
    # This variable using the user's input of the question below to gain the users request
    # for the Encode, or decode service or to quit the program
    service = input(
        "'Encode' or 'decode' to start program or 'quit' to cancel\n ").lower()
    if service == "quit" or service == "q":
        system_on == True
        print("------------------------------")
        print("\n You have quit the program\n")
        print("------------------------------")
    # if encode service is requested the program will call the encode function
    elif service == "encode":
        encode_msg = input("\nWhats your message you would like to convert to morse code.\n")
        encode_msg = encode_msg.upper()
        function_encode(encode_msg)
    # if Decode service is requested the program will call the decode function
    elif service == "decode":
        decode_msg = input("\nPlace morse code here:\n ")
        function_decode(decode_msg)
    # If no valid input is found this is the error message
    # The program will display this and continue to ask for user request
    else:
        print("\nNo valid input.\n")