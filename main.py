from morse_code_converter import MorseConverter as morse

code_is_running = True

while code_is_running:

    user_options = input('Choose from "encrypt" or "decrypt": ')

    if user_options == 'encrypt':
        message_to_encrypt = input('Type the message you wish to encrypt: ')
        encrypted_message = morse().encrypt(message_to_encrypt)
        print(encrypted_message)

    elif user_options == 'decrypt':
        message_to_decrypt = input('Morse code to decrypt: ').strip()
        decrypted_message = morse().decrypt(message_to_decrypt)
        print(decrypted_message)

    else:
        print('Wrong choice of function!')
        continue

    cut_conncection = input('Do you wish to cut the connection "Y"/ "N"? ').title()

    if cut_conncection != 'N':
        break

