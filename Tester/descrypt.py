LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'


def decryptCipher(message, key):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)  # get the number of the symbol
            num = num - key
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
    return translated


if __name__ == '__main__':
    msg = input("Message: ")
    length = len(LETTERS)
    for key in range(0, length+1):
        print(str(key), " " + decryptCipher(msg, key))
        print("")
