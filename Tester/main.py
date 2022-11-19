from fastapi import FastAPI
import uvicorn
import requests
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'


def encryptCipher(message, key):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)  # get the number of the symbol
            num = num + key
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
    return translated


app = FastAPI()


@app.get("/encrypt/{key}")
def morty(key: str):
    response_API = requests.get(
        'https://rickandmortyapi.com/api/character/290')
    data = response_API.text
    data = data.replace('"', "'")
    return encryptCipher(data, int(key))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=23450)
