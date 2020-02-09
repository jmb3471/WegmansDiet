from flask import *
from wegmans_api.wm_products import *
from diet.FoodItem import foodObject
from diet.ShoppingList import *
from diet.parseSearch import *
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

@app.route('/sendDataToBack',methods=['POST'])
def sendDatatoBack():
    data=request.get_json()
    type = data['action']
    if type == 'remove':
        foodObjectThing = data['object']
        sku = foodObjectThing['sku']
        actualObject = wm_products.get_product(sku)
        name = actualObject['name']
        nutrients = actualObject['nutrients']
        price = wm_products.get_price(sku, 1)
        price = price['price']
        foodObjectThing = foodObject(name,price,nutrients,sku)
        remove_item(foodObjectThing,1)
        print('We Gucci if this appears')
        return jsonify(data['object'])
    elif type == 'add':
        foodObjectThing = data['object']
        sku = foodObjectThing['sku']
        actualObject = wm_products.get_product(sku)
        name = actualObject['name']
        nutrients = actualObject['nutrients']
        price = wm_products.get_price(sku, 1)
        price = price['price']
        foodObjectThing = foodObject(name,price,nutrients,sku)
        add_item(foodObjectThing,1)
        print('We Gucci if this appears')
        return jsonify(data['object'])
    elif type == 'search':
        name = data['name']
        jsonfile = wm_products.search_products(name)
        results = jsonfile['results']
        results = parse(results)
        return jsonify(results)

if __name__ == '__main__':
    app.run()
