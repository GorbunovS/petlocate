from flask import Flask


app = Flask(__name__, static_folder='static/dist')

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
def catch_all(path):
    if path != "" and path.exists():
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
