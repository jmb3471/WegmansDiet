from ShoppingList import *
from FoodItem import *
from WeeklyValues import SEX

from diet.FoodItem import foodObject
from diet.ShoppingList import ShoppingList


def main():
	shopping_cart = ShoppingList(SEX.Male)
	fake_food = foodObject("fake_food", 69, {"zinc": 12, "iron": 2, "calcium": 4}, "shelf")
	print(fake_food.name)
	shopping_cart.add_item(fake_food, 1)
	print(shopping_cart.toString())

	i = 0
	while (True):
		i += 1
		info = input("Enter an item")
		info_split = info.split(" ")
		val = int(info_split[3])
		vitamins = {info_split[2]: val}
		food = foodObject(info_split[0], info_split[1], vitamins, info_split[4])
		quantity = int(info_split[5])
		shopping_cart.add_item(food, quantity)
		print(shopping_cart.toString())




if __name__ == '__main__':
	main()