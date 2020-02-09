from flask import *

app = Flask(__name__)

@app.route('/processjson',methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    cost = data['cost']
    return jsonify({'name':name,'cost':cost})


if __name__ == '__main__':
    app.run(debug=True)
