"""
Weekly dietary information on average based on FDA recommendations and Nutrition Label Guidelines
File: WeeklyValues.py
@author Jonathan Baxley
"""
import enum



#Vitamins in milligrams
ZINC = 15.00 * 7.00
POTASSIUM = 3500.00 * 7.00
SODIUM = 2400.00 * 7.00
IRON = 18.00 * 7.00
CALCIUM = 268.00 * 7.00

#In Kcal
CALORIES_MALE = 2500.00 * 7.00
CALORIES_FEMALE = 2000.00 * 7.00

#in grams
TOT_FAT = 66.67 * 7.00 * 1000
TOT_CARBS = 283.33 * 7.00 * 1000
CHOLESTEROL = 333.33 * 7.00 * 1000
PROTEIN = 50.00 * 7.00 * 1000
DIETARY_FIBER = 20.00 * 7.00 * 1000

#SEX
class SEX(enum.Enum):
    Male = 0,
    Female = 1,
    Prefer_not = 2
#amount of time
class TIME(enum.Enum):
    Week = 1.0
    Day = 1/7


