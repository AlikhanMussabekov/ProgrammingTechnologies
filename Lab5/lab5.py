"""
Вход: файл guess.txt содержащий имена для угадывания
(например из http://www.biographyonline.net/people/famous-100.html можно взять имена)

Написать игру "Угадай по фото"

3 уровня сложности:
1) используются имена только 1-10
2) имена 1-50
3) имена 1-100

- из используемых имен случайно выбрать одно
- запустить поиск картинок в Google по выбранному
- получить ~30-50 первых ссылок на найденные по имени изображения
- выбрать случайно картинку и показать ее пользователю для угадывания
  (можно выбрать из выпадающего списка вариантов имен)
- после выбора сказать Правильно или Нет

п.с. сделать серверную часть, т.е. клиент играет в обычном браузере обращаясь к веб-серверу.

п.с. для поиска картинок желательно эмулировать обычный пользовательский запрос к Google
или можно использовать и Google image search API
https://ajax.googleapis.com/ajax/services/search/images? или др. варианты
НО в случае API нужно предусмотреть существующие ограничения по кол-ву запросов
т.е. кешировать информацию на случай исчерпания кол-ва разрешенных (бесплатных)
запросов или другим образом обходить ограничение. Т.е. игра не должна прерываться после N запросов (ограничение API)

п.с. желательно "сбалансировать" параметры поиска (например искать только лица,
использовать только первые 1-30 найденных и т.п.)
для минимизации того что найденная картинка не соответствует имени
"""

import requests
import random
import os
import cv2
import numpy as np

from PIL import Image
from flask import request
from flask import Flask
from flask_cors import CORS

game_config = {'1': 10, '2': 20, '3': 30}

image_path = "/Users/a.musabekov/labs/ProgrammingTechnologies/PythonLabs/Lab5/new_image.jpg"
cascade_path = "/Users/a.musabekov/labs/ProgrammingTechnologies/PythonLabs/Lab5/haarcascade_frontalface_default.xml"
names_path = "/Users/a.musabekov/labs/ProgrammingTechnologies/PythonLabs/Lab5/names"

app = Flask(__name__)
CORS(app)

def request_images(name):
    endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": name,
        "num": 10,
        "imgSize": "medium",
        "searchType": "image",
        "filetype": "jpg",
        "key": "API_SECRET_KEY",
        "cx": "API_CX"
    }
    
    response = requests.get(endpoint, params=params).json()
    if 'items' in response:
        try:
            return list(map(lambda x: x['link'], response['items']))
        except(IndexError, TypeError):
            return 'Server Error'
    return 'No Items in response'


def save_image(link):
    response = requests.get(link)
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            f.write(response.content)


def choose_image(images):
    for image in images:
        save_image(image)
        if (has_face_on_image(image_path)):
            return image


def has_face_on_image(path):
    faceCascade = cv2.CascadeClassifier(cascade_path)
    
    gray = Image.open(path).convert('L')
    image = np.array(gray, 'uint8')

    faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces) > 0


def random_names(count):
    with open(names_path, "r") as f:
        names = set()
        names_file = list(f)
        while len(names) < count:
            names.add(random.choice(names_file).rstrip())
        return list(names)


@app.route('/startgame', methods=['GET'])
def start_game():
    lvl = request.args.get('lvl')
    
    names = random_names(game_config[lvl])
    answer_name = random.choice(names)
    
    images = request_images(answer_name)
    image_link = choose_image(images)
    return {'image': image_link, 'names': names, 'answer': answer_name}

   
if __name__ == '__main__':
    app.run()
