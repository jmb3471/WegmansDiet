
class foodObject:
    def __init__(self,name,cost,nutrition_facts):
        self.name = name
        #price per unit or pound.
        self.cost = cost
        #nutrition facts are a key:value pair, with string:value
        self.nutrition_facts = nutrition_facts

    def get_nut_specific(self,thing):
        if (self.nutrition_facts == []):
            return 0
        for x in self.nutrition_facts:
            if x['type'] == thing:
                quantity = x['quantity']
                dailypercent = x['dailyValuePercent']
                if quantity != '' and quantity != 'None':
                    try:
                        return float(quantity)
                    except:
                        return 0
                else:
                    return 0
            else:
                return 0

    def toString(self):
        return(self.name + " costs $"+ str(self.cost) + " ")


