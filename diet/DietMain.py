"""
File: DietMain.py
@authors: Jonathan Baxley, Ezequiel Salas
This file takes a json file as input and returns a json file to the server/app
"""


from ShoppingList import *
from FoodItem import *
from WeeklyValues import *
from wegmans_api import wm_products
import json
from diet.FoodItem import foodObject
from diet.ShoppingList import ShoppingList


"""
Main function
@author: Jonathan Baxley, Ezequiel Salas
Work in progress ...
"""
def main():
	shopping_list = ShoppingList(SEX.Male, TIME.Day)
	json_file = wm_products.get_product(435178)
	print(json_file)
	name = json_file['name']
	price = wm_products.get_price(391882, 1)
	price = price['price']
	nutrition = json_file['nutrients']
	print(nutrition)

	example = foodObject(name, price, nutrition)
	shopping_list.add_item(example, 2)

	sendToJson(shopping_list)


"""
Sends the shopping list information to a json file
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
		'Items': shopping_list.items

	})

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)


if __name__ == '__main__':
	main()