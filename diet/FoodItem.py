
class foodObject():
    def __init__(self,name,cost,nutrition_facts,location):
        self.name = name
        self.cost = cost
        self.nutrition_facts = nutrition_facts
        self.location = location

    def get_nut_specific(self,thing):
        if thing in self.nutrition_facts:
            return self.nutrition_facts[thing]
        else:
            return 0


