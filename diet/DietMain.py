from ShoppingList import *
from FoodItem import *
from WeeklyValues import *
from wegmans_api import wm_products
import json
from diet.FoodItem import foodObject
from diet.ShoppingList import ShoppingList

def main():
	#store = wm_stores.get_stores()
	#print(store)
	shopping_list = ShoppingList(SEX.Male, TIME.Day)
	json_file = wm_products.search_products("yogurt")
	json_file = wm_products.get_product(366382)
	print(json_file)
	name = json_file['name']
	price = wm_products.get_price(391882, 1)
	price = price['price']
	nutrition = json_file['nutrients']

	print(nutrition)

	example = foodObject(name, price, nutrition)
	string = example.get_nut_specific("Calcium")
	shopping_list.add_item(example, 2)

	print(shopping_list.calories)


if __name__ == '__main__':
	main()