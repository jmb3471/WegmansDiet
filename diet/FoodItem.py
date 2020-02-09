"""
File:FoodItem.py
@authors: Jonathan Baxley, Ezequiel Salas
Class object for a food item. Generic data structure
to keep track of information for any food item.
"""


class foodObject:
    def __init__(self,name,cost,nutrition_facts, sku):
        self.name = name
        #price per unit or pound.
        self.cost = cost
        #nutrition facts are a key:value pair, with string:value
        self.nutrition_facts = nutrition_facts
        self.sku = sku

    def get_nut_specific(self, thing):
        """
        Returns the nutrition value for the
        specified type of nutrition, in miligrams
        :param thing: String name of nutrition
        :return: float amount of nutrition in miligrams
        """
        if (self.nutrition_facts == []):
            return 0
        #iterate through the nutrition dictionary
        for x in self.nutrition_facts:
            #if the current key equals the one we are looking for
            if x['type'] == thing:
                quantity = x['quantity']
                #if there exists something in the quantity
                if quantity != '' and quantity != 'None':
                    try:
                        quantity_split = quantity.split(" ")
                        float_quant = float(quantity_split[0])
                        if (len(quantity_split) > 1):
                            #check to see if the value is in grams
                            if (quantity_split[1] == 'g'):
                                #convert to miligrams
                                float_quant = float_quant * 1000
                        return float_quant
                    except:
                        return 0
                else:
                    return 0
        else:
            return 0

    def toString(self):
        """
        :return: name,cost
        """
        return self.name + ","+str(self.cost)

