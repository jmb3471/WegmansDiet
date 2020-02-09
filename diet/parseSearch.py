from wegmans_api import wm_products
from diet.FoodItem import foodObject
def parse(list):
    new_dict ={}
    for dict in list:
        sku = dict['sku']
        #print(sku)
        try:
            product_json = wm_products.get_product(sku)
            name = product_json['name']
            price = wm_products.get_price(sku,3)
            price = price['price']
            nutrition = product_json['nutrients']
            food = foodObject(name,0,nutrition,sku)
            new_dict[name]={
                "name":name,
                'sku':sku
            }
        except (Exception):
            print()
    return new_dict

