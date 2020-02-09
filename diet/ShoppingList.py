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

            self.items.append(item.toString)
            self.zinc += item.get_nut_specific("Zinc")
            self.iron += item.get_nut_specific("Iron")
            self.sodium += item.get_nut_specific("Sodium")
            self.calcium += item.get_nut_specific("Calcium")
            self.calories += item.get_nut_specific("Calories")
            self.tot_fat += item.get_nut_specific("Total Fat")
            self.tot_carbs += item.get_nut_specific("Total Carbohydrate")
            self.protein += item.get_nut_specific("Protein")
            self.dietary_fiber += item.get_nut_specific("Dietary Fiber")
            self.cholesterol += item.get_nut_specific("Cholesterol")

        self.check_nut()


    #checks nutrition information of the shopping cart
    def check_nut(self):
        zinc_amount = ZINC*self.time.value
        iron_amount = IRON*self.time.value
        sodium_amount = SODIUM*self.time.value
        calories_amount = CALORIES_FEMALE if self.sex.value else CALORIES_MALE
        tot_fat_amount = TOT_FAT*self.time.value
        tot_carb_amount = TOT_CARBS*self.time.value
        protein_amount = PROTEIN*self.time.value
        dietary_fiber_amount = DIETARY_FIBER*self.time.value
        cholesteral_amount = CHOLESTEROL*self.time.value
        calcium_amount = CALCIUM*self.time.value
        if self.zinc < (zinc_amount-zinc_amount*0.1):
            zinc_missing = zinc_amount-self.zinc
            if self.time == TIME.Week:
                print("You are missing "+str(zinc_missing)+"mg for a weekly intake of zinc")
            else:
                print("You are missing "+str(zinc_missing)+"mg for today's intake of zinc")
        elif self.zinc > (zinc_amount+zinc_amount*0.1):
            zinc_over = self.zinc - zinc_amount
            if self.time == TIME.Week:
                print("You are over the recommended weekly intake of zinc by "+str(zinc_over)+"mg")
            else:
                print("You are over the recommended daily intake of zinc by " +str(zinc_over)+"mg")
        else:
            print("You've gotten enough zinc")

        if self.iron < (iron_amount-iron_amount*0.1):
            iron_missing = iron_amount-self.iron
            if self.time == TIME.Week:
                print("You are missing "+str(iron_missing)+"mg for a weekly intake of iron")
            else:
                print("You are missing "+str(iron_missing)+"mg for a daily intake of iron")
        elif self.iron > (iron_amount+iron_amount*0.1):
            iron_over = self.iron - iron_amount
            if self.time == TIME.Week:
                print("You are over the recommended weekly intake of iron by "+str(iron_over)+"mg")
            else:
                print("You are over the recommended daily intake of iron by "+str(iron_over)+"mg")
        else:
            print("You've gotten enough iron")
        ####
        ####
        if self.sodium < (sodium_amount-sodium_amount*0.1):
            sodium_missing = sodium_amount-self.sodium
            if self.time == TIME.Week:
                print("You are missing "+str(sodium_missing)+"mg for a weekly intake of sodium")
            else:
                print("You are missing "+str(sodium_missing)+"mg for a daily intake of sodium")
        elif self.sodium > (sodium_amount-sodium_amount*0.1):
            sodium_over = self.sodium - sodium_amount
            if self.time == TIME.Week:
                print("You are over the recommended weekly intake of sodium by "+str(sodium_over)+"mg")
            else:
                print("You are over the recommended daily intake of sodium by "+str(sodium_over)+"mg")
        else:
            print("You've gotten enough sodium")
        if self.calories < (calories_amount-calories_amount*0.1):
            calories_missing = calories_amount-self.calories
            if self.time == TIME.Week:
                print("You are missing "+str(calories_missing)+" calories for a weekly intake")
            else:
                print("You are missing "+str(calories_missing)+" calories for a daily intake")
        elif self.calories > (calories_amount+calories_amount*0.1):
            calories_over = self.calories - calories_amount
            if self.time == TIME.Week:
                print("You are over "+str(calories_over)+" calories for a weekly intake")
            else:
                print("You are over "+str(calories_over)+" calories for a daily intake")
        else:
            print("You've gotten enough calories")

        if self.tot_fat < (tot_fat_amount-tot_fat_amount*0.1):
            total_fat_missing = tot_fat_amount-self.tot_fat
            if self.time == TIME.Week:
                print("You are missing "+str(total_fat_missing)+"mg for a weekly intake of total fats")
            else:
                print("You are missing"+str(total_fat_missing)+"mg for a daily intake of total fats")
        elif self.tot_fat > (tot_fat_amount+tot_fat_amount*0.1):
            total_fat_over = self.tot_fat - tot_fat_amount
            if self.time == TIME.Week:
                print("You are over "+str(total_fat_over)+"mg for a weekly intake of total fats")
            else:
                print("You are over "+str(total_fat_over)+"mg for a daily intake of total fats")
        else:
            print("You've gotten enough total fat")
        if self.tot_carbs < (tot_carb_amount-tot_carb_amount*0.1):
            total_carb_missing = tot_carb_amount-self.tot_carbs
            if self.time == TIME.Week:
                print("You are missing "+str(total_carb_missing)+"mg for a weekly intake of total carbs")
            else:
                print("You are missing "+str(total_carb_missing)+"mg for a daily intake of total carbs")
        elif self.tot_carbs > (tot_carb_amount+tot_carb_amount*0.1):
            total_carb_over = self.tot_carbs -tot_carb_amount
            if self.time == TIME.Week:
                print("You are over "+str(total_carb_over)+"mg for a weekly intake of total carbs")
            else:
                print("You are over "+str(total_carb_over)+"mg for a daily intake of total carbs")
        else:
            print("You've gotten enough carbs")


        if self.protein < (protein_amount-protein_amount*0.1):
            protein_missing = protein_amount-self.protein
            if self.time == TIME.Week:
                print("You are missing "+str(protein_missing)+"mg for a weekly intake of protein")
            else:
                print("You are missing "+str(protein_missing)+"mg for a daily intake of protein")
        elif self.protein > (protein_amount+protein_amount*0.1):
            protein_over = self.protein-protein_amount
            if self.time == TIME.Week:
                print("You are over "+str(protein_over)+"mg for a weekly intake of protein")
            else:
                print("You are over "+str(protein_over)+"mg for a daily intake of protein")
        else:
            print("You've gotten enough protein")

        if self.dietary_fiber < (dietary_fiber_amount-dietary_fiber_amount*0.1):
            dietary_fiber_missing = dietary_fiber_amount-self.dietary_fiber
            if self.time == TIME.Week:
                print("You are missing "+str(dietary_fiber_missing)+"mg for a weekly intake of dietary fiber")
            else:
                print("You are missing "+str(dietary_fiber_missing)+"mg for a daily intake of dietary fiber")
        elif self.dietary_fiber > (dietary_fiber_amount+dietary_fiber_amount*0.1):
            dietary_fiber_over = self.dietary_fiber-dietary_fiber_amount
            if self.time == TIME.Week:
                print("You are over "+str(dietary_fiber_over)+"mg for a weekly intake of dietary fiber")
            else:
                print("You are over "+str(dietary_fiber_over)+"mg for a daily intake of dietary fiber")
        else:
            print("You've gotten enough fiber")


        if self.cholesterol < (cholesteral_amount-cholesteral_amount*0.1):
            cholesteral_missing = cholesteral_amount-self.cholesterol
            if self.time == TIME.Week:
                print("You are missing "+str(cholesteral_missing)+"mg for a weekly intake of cholesteral")
            else:
                print("You are missing "+str(cholesteral_missing)+"mg for a daily intake of cholesteral")
        elif self.cholesterol > (cholesteral_amount+cholesteral_amount*0.1):
            cholesteral_over = self.cholesterol-cholesteral_amount
            if self.time == TIME.Week:
                print("You are over "+str(cholesteral_over)+"mg for weekly intake of cholesteral")
            else:
                print("You are over "+str(cholesteral_over)+"mg for a daily intake of cholesteral")
        else:
            print("You've gotten enough cholesterol")

        if self.calcium < (calories_amount-calories_amount*0.1):
            calcium_missing = calcium_amount-self.calcium
            if self.time == TIME.Week:
                print ("You are missing "+str(calcium_missing)+"mg for a weekly intake of calcium")
            else:
                print ("You are missing "+str(calcium_missing)+"mg for a daily intake of calcium")
        elif self.calcium > (calcium_amount+calcium_amount*0.1):
            calcium_over = self.calcium - calcium_amount
            if self.time == TIME.Week:
                print ("You are over "+str(calcium_over)+"mg for a weekly intake of calcium")
            else:
                print("You are over "+str(calcium_over)+"mg for a daily intake of calcium")
        else:
            print("enough calcium")
