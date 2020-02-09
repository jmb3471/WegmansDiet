"""
File: DietMain.py
@authors: Jonathan Baxley, Ezequiel Salas
This file takes a json_file file as input and returns a json_file file to the server/app
"""


from diet.FoodItem import *
from diet.ShoppingList import *
from diet.WeeklyValues import *
from wegmans_api import wm_products
import json
from diet.FoodItem import foodObject



"""
Main function
@author: Jonathan Baxley, Ezequiel Salas
Work in progress ...
"""
def main():
	json_file = wm_products.get_product(435178)
	name = json_file['name']
	price = wm_products.get_price(391882, 1)
	price = price['price']
	nutrition = json_file['nutrients']
	example = foodObject(name, price, nutrition, 391882)
	add_item(example, 2)

	remove_item(example, 1)

	sendToJson(SHOPPING_LIST)


"""
Sends the shopping list information to a json_file file
@author: Jonathan Baxley
@:param takes a shopping list as input
"""
def sendToJson(shopping_list):
	data = {}
	data['Nutrients'] = []
	data['Info'] = []
	data['Nutrients'].append({
		'Zinc': shopping_list.zinc,
		'Iron': shopping_list.iron,
		'Sodium': shopping_list.sodium,
		'Calcium': shopping_list.calcium,
		'Calories': shopping_list.calories,
		'Total Fat': shopping_list.tot_fat,
		'Total Carbohydrate': shopping_list.tot_carbs,
		'Protein': shopping_list.protein,
		'Cholesterol': shopping_list.cholesterol,
		'Dietary Fiber': shopping_list.dietary_fiber
	})
	data['Info'].append({
		'Sex': shopping_list.sex.value,
		'Time': shopping_list.time.value,
		'Items': shopping_list.toList()

	})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)


if __name__ == '__main__':
	main()