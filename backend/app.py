from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

items = [
    {
        'id': 1,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Около часа назад',
        'location': 'г. Москва, ул. Арбат',
        'comment': 'Отзывается на кличку Тесла. Любит есть какашки',
        'position': [37.5956, 55.7522]  # Долгота, Широта
    },
    {
        'id': 2,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Найден',
        'type': 'dog',
        'time': 'Около двух часов назад',
        'location': 'г. Москва, Красная площадь',
        'comment': 'Отзывается на кличку Бобик. Любит бегать за палками',
        'position': [37.6204, 55.7541]  # Долгота, Широта
    },
    {
        'id': 3,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Тверская',
        'comment': 'Отзывается на кличку Мурка. Боится громких звуков',
        'position': [37.6125, 55.7592]  # Долгота, Широта
    },
    {
        'id': 4,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Найден',
        'type': 'dog',
        'time': 'Вчера вечером',
        'location': 'г. Москва, Парк Горького',
        'comment': 'Отзывается на кличку Рекс. Любит играть с детьми',
        'position': [37.6036, 55.7294]  # Долгота, Широта
    },
    {
        'id': 5,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня днем',
        'location': 'г. Москва, ВДНХ',
        'comment': 'Отзывается на кличку Васька. Любит сидеть на деревьях',
        'position': [37.6386, 55.8296]  # Долгота, Широта
    },
    {
        'id': 6,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'dog',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Лубянка',
        'comment': 'Отзывается на кличку Шарик. Дружелюбен к прохожим',
        'position': [37.6261, 55.7596]  # Долгота, Широта
    },
    {
        'id': 7,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Варварка',
        'comment': 'Отзывается на кличку Бегемот. Любит лазить по крышам',
        'position': [37.6306, 55.7526]  # Долгота, Широта
    },
    {
        'id': 8,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'dog',
        'time': 'Сегодня днем',
        'location': 'г. Москва, ул. Сретенка',
        'comment': 'Отзывается на кличку Пушок. Любит прятаться в кустах',
        'position': [37.6176, 55.7681]  # Долгота, Широта
    },
    {
        'id': 9,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Мясницкая',
        'comment': 'Отзывается на кличку Барсик. Любит лежать на солнце',
        'position': [37.6342, 55.7654]  # Долгота, Широта
    },
    {
        'id': 10,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'dog',
        'time': 'Сегодня днем',
        'location': 'г. Москва, ул. Покровка',
        'comment': 'Отзывается на кличку Жучка. Очень игривый',
        'position': [37.6446, 55.7597]  # Долгота, Широта
    },
    {
        'id': 11,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Остоженка',
        'comment': 'Отзывается на кличку Лёва. Любит мяукать по утрам',
        'position': [37.6053, 55.7435]  # Долгота, Широта
    },
    {
        'id': 12,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'dog',
        'time': 'Сегодня днем',
        'location': 'г. Москва, ул. Маросейка',
        'comment': 'Отзывается на кличку Пират. Боится воды',
        'position': [37.6421, 55.7577]  # Долгота, Широта
    },
    {
        'id': 13,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Моховая',
        'comment': 'Отзывается на кличку Симба. Любит играть с игрушками',
        'position': [37.6151, 55.7558]  # Долгота, Широта
    },
    {
        'id': 14,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'dog',
        'time': 'Сегодня днем',
        'location': 'г. Москва, ул. Таганская',
        'comment': 'Отзывается на кличку Джек. Обожает гулять по вечерам',
        'position': [37.6578, 55.7422]  # Долгота, Широта
    },
    {
        'id': 15,
        'photo': 'https://via.placeholder.com/100',
        'status': 'Утерян',
        'type': 'cat',
        'time': 'Сегодня утром',
        'location': 'г. Москва, ул. Садовая',
        'comment': 'Отзывается на кличку Том. Любит кушать рыбу',
        'position': [37.6217, 55.7557]  # Долгота, Широта
    }
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
