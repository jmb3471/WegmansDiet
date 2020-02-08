"""
Parses JSON FILE To add to each object that comes in to a shopping list object
File: ShoppingList.py
@authors: Jonathan Baxley
"""


class ShoppingList:
    def __init__(self, sex):
        self.sex = sex
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


    #Prints string list of items s
    @override
    def toString(self):
        str = ""
        for x in self.items:
            str += x.toString()

        str += "."
        return str



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


    def check_nut(self):
        if self.zinc < ZINC:
            print("Not enough zinc for the week")
        else:
            print("You've gotten enough zinc")
        if self.potassium < POTASSIUM:
            print("Not enough potassium for the week")
        else:
            print("You've gotten enough potassium")
        if self.iron < IRON:
            print("Not enough iron for the week")
        else:
            print("You've gotten enough iron")
        if self.sodium < SODIUM:
            print("Not enough sodium for the week")
        else:
            print("You've gotten enough sodium")
        if (self.sex == SEX.Male):
            if (self.calories < CALORIES_MALE):
                print("Not enough calories")
            else:
                print("Enough Calories")
        else:
            if (self.calories < CALORIES_FEMALE):
                print("Not enough calories")
            else:
                print("Enough Calories")
        if self.tot_fat < TOT_FAT:
            print("Not enough fat for the week")
        else:
            print("You've gotten enough fat")
        if self.tot_carbs < TOT_CARBS:
            print("Not enough carbs for the week")
        else:
            print("You've gotten enough carbs")
        if self.protein < PROTEIN:
            print("Not enough protein for the week")
        else:
            print("You've gotten enough protein")
        if self.dietary_fiber < DIETARY_FIBER:
            print("Not enough fiber for the week")
        else:
            print("You've gotten enough fiber")
        if self.cholesterol < CHOLESTEROL:
            print("Not enough cholesterol for the week")
        else:
            print("You've gotten enough cholesterol")
