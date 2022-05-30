class City:
    def __init__(self, name, straight_line_distance):
        self.name = name
        self.straightLineDistance = straight_line_distance
        self.roads = []

    def __repr__(self):
        return "City(name: " + str(self.name) + ", straightLineDistance: " \
               + str(self.straightLineDistance) + ", roads: " + str(self.roads) + ")"

