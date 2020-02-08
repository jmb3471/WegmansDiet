"""
Parses JSON FILE To add to each object that comes in to a shopping list object
File: ShoppingList.py
@authors: Jonathan Baxley
"""


class ShoppingList:
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
            self.zinc += item.get_nut_specific("zinc")
            self.potassium += item.get_nut_specific("potassium")
            self.iron += item.get_nut_specific("iron")
            self.sodium += item.get_nut_specific("sodium")
            self.calcium += item.get_nut_specific("calcium")
            self.calories += item.get_nut_specific("calories")
            self.tot_fat += item.get_nut_specific("tot_fat")
            self.tot_carbs += item.get_nut_specific("tot_carbs")
            self.protein += item.get_nut_specific("protein")
            self.dietary_fiber += item.get_nut_specific("dietary_fiber")
            self.cholesterol += item.get_nut_specific("cholesterol")


