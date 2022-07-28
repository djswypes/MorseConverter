MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

class MorseConverter():

    def __init__(self) -> None:
        self.cipher = ''
        self.decipher = ''

    def encrypt(self, message):

        for letter in message.upper():
            
            if letter == ' ':
                self.cipher += ' '

            if letter in MORSE_CODE_DICT:
                self.cipher += MORSE_CODE_DICT[letter] + ' '

        return self.cipher

    def decrypt(self, morse_code):
    # Ask for the word
        morse_code += " "
        citext = ''
        error = 0

        #check for space
        for code in morse_code:

            # checks for space
            if code != ' ':

                citext += code

                i = 0
            
            else:
                
                i += 1

                if i == 2:

                    self.decipher += ' '
                
                else:
                    try:
                        self.decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    
                    except:
                        error += 1

                    finally:
                        citext = ''

        if error > 0:
            return 'Invalid Morse Code.'

        return self.decipher


