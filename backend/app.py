from flask import Flask, jsonify
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {
            'id': 1,
            'photo': 'https://via.placeholder.com/100',
            'status': 'Утерян',
            'type': 'cat',
            'time': 'Около часа назад',
            'location': 'г. Реутов Улица Октября',
            'comment': 'Отзывается на кличку Тесла. Любит есть какашки',
            'position': [55.760, 37.620]  # Координаты для маркера
        }
        # Добавьте другие предметы здесь
    ]
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True)