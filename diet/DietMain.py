from ShoppingList import *
from FoodItem import *
from WeeklyValues import SEX

def main():
	shopping_cart = ShoppingList(SEX.Male)
	fake_food = foodObject("fake_food",69,{"zinc":12,"iron":2,"calcium":4},"shelf")
	print(fake_food.name)
	shopping_cart.add_item(fake_food, 1)
	print(shopping_cart.toString())

if __name__ == '__main__':
	main()