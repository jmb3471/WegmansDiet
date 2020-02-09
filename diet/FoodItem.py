
class foodObject:
    def __init__(self,name,cost,nutrition_facts):
        self.name = name
        #price per unit or pound.
        self.cost = cost
        #nutrition facts are a key:value pair, with string:value
        self.nutrition_facts = nutrition_facts

    def get_nut_specific(self, thing):
        if (self.nutrition_facts == []):
            return 0
        for x in self.nutrition_facts:
            if x['type'] == thing:
                quantity = x['quantity']

                if quantity != '' and quantity != 'None':
                    try:
                        quantity_split = quantity.split(" ")
                        float_quant = float(quantity_split[0])
                        if (len(quantity_split) > 1):
                            if (quantity_split[1] == 'g'):
                                float_quant = float_quant * 1000
                        print(quantity_split[0])
                        return float_quant
                    except:
                        return 0
                else:
                    return 0
        else:
            return 0


    def toString(self):
        return self.name + " costs $"+ str(self.cost) + " "


