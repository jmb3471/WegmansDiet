"""
File: DietMain.py
@authors: Jonathan Baxley, Ezequiel Salas
This file takes a json_file file as input and returns a json_file file to the server/app
"""


from ShoppingList import *
from FoodItem import *
from WeeklyValues import *
from wegmans_api import wm_products
import json_file
from diet.FoodItem import foodObject
from diet.ShoppingList import ShoppingList


SHOPPING_LIST = ShoppingList(SEX.Male, TIME.Day)

"""
Main function
@author: Jonathan Baxley, Ezequiel Salas
Work in progress ...
"""
def main():
	shopping_list = ShoppingList(SEX.Male, TIME.Day)
	json_file = wm_products.get_product(435178)
	name = json_file['name']
	price = wm_products.get_price(391882, 1)
	price = price['price']
	nutrition = json_file['nutrients']

	example = foodObject(name, price, nutrition, 391882)
	shopping_list.add_item(example, 2)

	sendToJson(shopping_list)


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
		'Items': shopping_list.items

	})

	with open('data.json_file', 'w') as outfile:
		json_file.dump(data, outfile)


if __name__ == '__main__':
	main()