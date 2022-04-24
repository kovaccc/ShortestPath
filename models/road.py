class Road:
    def __init__(self, end_city, cost):
        self.endCity = end_city
        self.cost = cost

    def toString(self):
        return "Road(endCity: " + str(self.endCity.toString()) + ", cost: " \
               + str(self.cost) + ")"
