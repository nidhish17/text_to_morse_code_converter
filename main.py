print("""
 _____  ________  _ _____    _____  ____    _      ____  ____  ____  _____   ____  ____  ____  _____
/__ __\/  __/\  \///__ __\  /__ __\/  _ \  / \__/|/  _ \/  __\/ ___\/  __/  /   _\/  _ \/  _ \/  __/
  / \  |  \   \  /   / \      / \  | / \|  | |\/||| / \||  \/||    \|  \    |  /  | / \|| | \||  \  
  | |  |  /_  /  \   | |      | |  | \_/|  | |  ||| \_/||    /\___ ||  /_   |  \__| \_/|| |_/||  /_ 
  \_/  \____\/__/\\  \_/      \_/  \____/  \_/  \|\____/\_/\_\\____/\____\  \____/\____/\____/\____\
                                                                                                                                                                                                                                                                                                                                                                                                              
\n*spaces will be replaced by '/'\n*Non Convertable Chars Will Be Replaced By '#'\ncommands--> [1.'#stop' - To Stop Using]\n
""")

def text_to_morse(user_text, morse_code_val):

    converted_text = ""

    for char in user_text.lower():
        if char.isspace():
            converted_text += "/"
        else:
            try:
                converted_text += morse_code_val[char]
            except:
                converted_text += "#"

    return converted_text
morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}
user_converting = True
while user_converting:
    print("TEXT --> MORSE")
    user_input = input("Enter The Text You Want To Convert Here: ")

    if user_input.startswith("#") and user_input == "#stop" :
        user_converting = False
    else:
        converted_text = text_to_morse(user_text= user_input, morse_code_val= morse_code)
        print(converted_text)