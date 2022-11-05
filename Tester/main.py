from fastapi import FastAPI
import uvicorn
import requests
import math


def encryptMessage(msg, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1
    return cipher


app = FastAPI()


@app.get("/encrypt/{key}")
def morty(key: str):
    response_API = requests.get(
        'https://rickandmortyapi.com/api/character/290')
    data = response_API.text
    data = data.replace('"', "'")
    return encryptMessage(data, key)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=23450)
