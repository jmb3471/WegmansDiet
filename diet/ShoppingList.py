"""
Parses JSON FILE To add to each object that comes in to a shopping list object
File: ShoppingList.py
@authors: Jonathan Baxley
"""
import FoodItem.py


class ShoppingList():
    def __init__(self, gender):
        self.gender = gender
        self.zinc = 0
        self.potassium = 0
        self.iron = 0
        self.sodium = 0
        self.calcium = 0
        self.calories = 0
        self.tot_fat = 0
        self.tot_carbs = 0
        self.protein = 0
        self.dietary_fiber = 0
        self.cholesterol = 0
        self.items = []


    #adds an item to the shopping list and all of its nutritional values
    def add_item(self, item, quantity):
        while (quantity > 0):
            quantity -= 1

            self.items.append(item)
            self.zinc += get_nut_specific(item, "zinc")
            self.potassium += get_nut_specific(item, "potassium")
            self.iron += get_nut_specific(item, "iron")
            self.sodium += get_nut_specific(item, "sodium")
            self.calcium += get_nut_specific(item, "calcium")
            self.calories += get_nut_specific(item, "calories")
            self.tot_fat += get_nut_specific(item, "tot_fat")
            self.tot_carbs += get_nut_specific(item, "tot_carbs")
            self.protein += get_nut_specific(item, "protein")
            self.dietary_fiber += get_nut_specific(item, "dietary_fiber")
            self.cholesterol += get_nut_specific(item, "cholesterol")

        return

