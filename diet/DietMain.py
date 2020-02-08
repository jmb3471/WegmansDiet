from ShoppingList import *
from FoodItem import *
from WeeklyValues import SEX

from wegmans_api import wm_products


import json

from diet.FoodItem import foodObject
from diet.ShoppingList import ShoppingList


def main():
	#json_file = wm_products.search_products("chobani")
	json_file = wm_products.get_product(435178)

	nutrients = json_file['nutrients']
	for x in nutrients:
		type = x['type']
		print(type)
		quantity = x['quantity']
		print(quantity)
	if ('Calcium' in nutrients):
		print(nutrients)
	else:
		print("\nnah")


if __name__ == '__main__':
	main()