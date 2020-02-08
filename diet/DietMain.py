from ShoppingList import *
from FoodItem import *
from WeeklyValues import SEX

from wegmans_api import wm_products


import json

from diet.FoodItem import foodObject
from diet.ShoppingList import ShoppingList


def main():
	json_file = wm_products.get_product(232669)
	print(json_file)

if __name__ == '__main__':
	main()