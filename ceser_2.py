""" The Caesar code.
 Instruction: the program asks you for options such as the language in which the message will be entered, what you want
  to do - encrypt the message or decrypt, the key. Please note that the program may not work correctly if you enter text
   that does not match the selected language. """

ru_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_code = ""


def ask_user():
    while True:
        language = input("Please select the language of your message - ru/en: ")
        if language == "ru":
            action = input("Do you want encrypt or decrypt - e/d: ")
            text = input("Your message:\n")
            key = int(input("Your key: \n"
                            "Attention: do not enter the key equal to 32, otherwise your message"
                            "will remain unencrypted or unencrypted!  "))
            return language, action, text, key
        elif language == "en":
            action = input("Do you want encrypt or decrypt - e/d: ")
            text = input("Your message: \n")
            key = int(input("Your key: \n "
                            "Attention: do not enter the key equal to 26, otherwise your message"
                            "will remain unencrypted or unencrypted "))
            return language, action, text, key
        else:
            print("You entered incorrect data, please try again - ru or en \n")
            continue


while True:
    language, action, text, key = ask_user()
    if action == 'e':
        if language == 'ru':
            for char in range(len(text)):
                if text[char] == text[char].lower() and text[char].isalpha():
                    text_code += ru_lower[ru_lower.find(text[char]) + key]
                elif text[char] == text[char].upper() and text[char].isalpha():
                    text_code += ru_upper[ru_upper.find(text[char]) + key]
                else:
                    text_code += text[char]
            print(f'Result: {text_code}')
            break
        if language == "en":
            for char in range(len(text)):
                if text[char] == text[char].lower() and text[char].isalpha():
                    text_code += en_lower[en_lower.find(text[char]) + key]
                elif text[char] == text[char].upper() and text[char].isalpha():
                    text_code += en_upper[en_upper.find(text[char]) + key]
                else:
                    text_code += text[char]
            print(f'Result: {text_code}')
            break
    elif action == 'd':
        if language == 'ru':
            for char in range(len(text)):
                if text[char] == text[char].lower() and text[char].isalpha():
                    text_code += ru_lower[ru_lower.find(text[char]) - key]
                elif text[char] == text[char].upper() and text[char].isalpha():
                    text_code += ru_upper[ru_upper.find(text[char]) - key]
                else:
                    text_code += text[char]
            print(f'Result: {text_code}')
            break
        if language == "en":
            for char in range(len(text)):
                if text[char] == text[char].lower() and text[char].isalpha():
                    text_code += en_lower[en_lower.find(text[char]) - key]
                elif text[char] == text[char].upper() and text[char].isalpha():
                    text_code += en_upper[en_upper.find(text[char]) - key]
                else:
                    text_code += text[char]
            print(f'Result: {text_code}')
            break






