from flask import *

app = Flask(__name__)

@app.route('/processjson',methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    cost = data['cost']
    return jsonify({'name':name,'cost':cost})

@app.route('/sendDataToFront',methods=['POST'])
def sendDataToFront():
    data=request.get_json()

    #code for sending data to front end
    #however they decide to handle receiving data
    return jsonify(data)

@app.rout('/sendDataToBack',methods=['POST'])
def sendDatatoBack():
    data=request.get_json()
    type = data['action']
    if type == 'remove':
        foodObject = data['object']


if __name__ == '__main__':
    app.run(debug=True)
