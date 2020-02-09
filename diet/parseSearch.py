from wegmans_api.wm_products import get_product,get_price
from diet.FoodItem import foodObject
def parse(list):
    new_dict =[]
    for dict in list:
        sku = dict['sku']
        product_json = get_product(sku)
        name = product_json['name']
        price = get_price(sku,3)
        price = price['price']
        nutrition = product_json['nutrients']
        food = foodObject(name,price,nutrition,sku)
        new_dict.append(food)
    return new_dict

