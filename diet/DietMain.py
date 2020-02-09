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
	while (True):
		inp = input("Enter a command (Press H for help):")
		if inp == 'r':
			print(SHOPPING_LIST.toList())
			inp = input("Which sku would you like to remove:")
			lst = SHOPPING_LIST.toList()
			for x in lst:
				if x == inp:
					remove_item(SHOPPING_LIST.return_item(x), 1)
			print("Item not in cart")
		elif inp == 's':
			inp = input("Search for an Item: ")
			products = wm_products.search_products(inp)
			products = products['results']
			lst = []
			for x in products:
				lst.append(x['name'])
				lst.append(x['sku'])
			print(lst)
		elif inp == 'a':
			inp = input("Pick a SKU: ")
			json_file = wm_products.get_product(inp)
			name = json_file['name']
			price = wm_products.get_price(inp, 1)
			price = price['price']
			nutrition = json_file['nutrients']
			example = foodObject(name, price, nutrition, inp)
			add_item(example, 1)
		elif inp == 'p':
			lst = []
			for x in SHOPPING_LIST.toList():
				lst.append(SHOPPING_LIST.return_item(x).toString())
			print(lst)
		elif inp == 'n':
			SHOPPING_LIST.check_nut()
		elif inp == 'h':
			print("Press r to remove item.")
			print("Press a to add an item.")
			print("Press s to search for an item.")
			print("Press p to print your shopping cart.")
			print("Press n for nutritional details and suggestions.")
			print("Press h for help.")



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