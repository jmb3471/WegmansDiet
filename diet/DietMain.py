from ShoppingList import *
from FoodItem import *
from WeeklyValues import SEX

def main():
	shopping_cart = ShoppingList(SEX.Male)
	fake_food = foodObject("fake_food",69,{"zinc":12,"iron":2,"calcium":4},"shelf")
	print(fake_food.name)

main()