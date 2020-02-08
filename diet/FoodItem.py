
class foodObject:
    def __init__(self,name,cost,nutrition_facts,location):
        self.name = name
        #price per unit or pound.
        self.cost = cost
        #nutrition facts are a key:value pair, with string:value
        self.nutrition_facts = nutrition_facts

    def get_nut_specific(self,thing):
        if thing in self.nutrition_facts:
            return self.nutrition_facts[thing]
        else:
            return 0
    def toString(self):
        return(self.name + " costs $"+ str(self.cost) + " ")


