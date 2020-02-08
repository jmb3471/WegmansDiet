import ShoppingList
import FoodItem
from WeeklyValues import SEX

def main():
	shopping_cart = ShoppingList(SEX.Male)
	fake_food = foodObject("fake_food",69,{"zinc":12,"iron":2,"calcium":4})
	print(fake_food.name)
	print("Hello World")

main()