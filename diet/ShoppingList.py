"""
Parses JSON FILE To add to each object that comes in to a shopping list object
File: ShoppingList.py
@authors: Jonathan Baxley
"""
from diet.WeeklyValues import *


class ShoppingList:
    def __init__(self, sex,time):
        self.sex = sex
        self.time = time
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
    def toString(self):
        str = ""
        for x in self.items:
            str += x.toString()

        str += ". "
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

        self.check_nut()


    #checks nutrition information of the shopping cart
    def check_nut(self):
        zinc_amount = ZINC*self.time.value
        potassium_amount = POTASSIUM*self.time.value
        iron_amount = IRON*self.time.value
        sodium_amount = SODIUM*self.time.value
        if self.zinc < (zinc_amount-zinc_amount*0.1):
            zinc_missing = zinc_amount-self.zinc
            if self.time == TIME.Week:
                print("You are missing "+str(zinc_missing)+"mg for a weekly intake of zinc")
            else:
                print("You are missing "+str(zinc_missing)+"mg for today's intake of zinc")
        elif self.zinc > (zinc_amount+zinc_amount*0.1):
            zinc_over = self.zinc - zinc_amount+zinc_amount*0.1
            if self.time == TIME.Week:
                print("You are over the recommended weekly intake of zinc by "+str(zinc_over)+"mg")
            else:
                print("You are over the recommended daily intake of zinc by " +str(zinc_over)+"mg")
        else:
            print("You've gotten enough zinc")

        if self.potassium < (potassium_amount-potassium_amount*0.1):
            potassium_missing = potassium_amount-self.potassium
            if self.time == TIME.Week:
                print("You are missing "+str(potassium_missing)+"mg for a weekly intake of potassium")
            else:
                print("You are missing "+str(potassium_missing)+"mg for a daily intake of potassium")
        elif self.potassium > (potassium_amount+potassium_amount*0.1):
            potassium_over = self.potassium - potassium_amount+potassium_amount*0.1
            if self.time == TIME.Week:
                print("You are over the recommended weekly intake of potassium by "+str(potassium_over)+"mg")
            else:
                print("You are over the recommended daily intake of potassium by "+str(potassium_over)+"mg")
        else:
            print("You've gotten enough potassium")

        if self.iron < (iron_amount-iron_amount*0.1):
            iron_missing = iron_amount-self.iron
            if self.time == TIME.Week:
                print("You are missing "+str(iron_missing)+"mg for a weekly intake of iron")
            else:
                print("You are missing "+str(iron_missing)+"mg for a daily intake of iron")
        elif self.iron > (iron_amount+iron_amount*0.1):
            iron_over = self.iron - iron_amount+iron_amount*0.1
            if self.time == TIME.Week:
                print("You are over the recommended weekly intake of iron by "+str(iron_over)+"mg")
            else:
                print("You are over the recommended daily intake of iron by "+str(iron_over)+"mg")
        else:
            print("You've gotten enough iron")
        ####
        ####
        if self.sodium < (SODIUM*self.time.value):
            print("Not enough sodium for the week")
        else:
            print("You've gotten enough sodium")
        if (self.sex == SEX.Male):
            if (self.calories < (CALORIES_MALE*self.time.value)):
                print("Not enough calories")
            else:
                print("Enough Calories")
        else:
            if (self.calories < (CALORIES_FEMALE*self.time.value)):
                print("Not enough calories")
            else:
                print("Enough Calories")
        if self.tot_fat < (TOT_FAT*self.time.value):
            print("Not enough fat for the week")
        else:
            print("You've gotten enough fat")
        if self.tot_carbs < (TOT_CARBS*self.time.value):
            print("Not enough carbs for the week")
        else:
            print("You've gotten enough carbs")
        if self.protein < (PROTEIN*self.time.value):
            print("Not enough protein for the week")
        else:
            print("You've gotten enough protein")
        if self.dietary_fiber < (DIETARY_FIBER*self.time.value):
            print("Not enough fiber for the week")
        else:
            print("You've gotten enough fiber")
        if self.cholesterol < (CHOLESTEROL*self.time.value):
            print("Not enough cholesterol for the week")
        else:
            print("You've gotten enough cholesterol")
