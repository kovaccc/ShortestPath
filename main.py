class Road:
    def __init__(self, end_city, cost):
        self.endCity = end_city
        self.cost = cost

    def toString(self):
        return "Road(endCity: " + str(self.endCity) + ", cost: " \
               + str(self.cost) + ")"


class City:
    def __init__(self, name, straight_line_distance):
        self.name = name
        self.straightLineDistance = straight_line_distance
        self.roads = []

    def toString(self):
        return "City(name: " + str(self.name) + ", straightLineDistance: " \
               + str(self.straightLineDistance) + ", roads: " + str(self.roads) + ")"


with open('Assignment 1 Spain map.txt') as knapsackFile:
    knapsack_file_lines = knapsackFile.readlines()
    cities = []

    for line in knapsack_file_lines[85:len(knapsack_file_lines)]:
        cityLine = [str(i) for i in line.split(" ")]
        cities.append(City(cityLine[0], int(cityLine[1])))

    for line in knapsack_file_lines[5:82]:
        roadLine = [str(i) for i in line.split(" ")]
        for city in cities:
            if city.name == roadLine[0]:
                city.roads.append(
                    Road(end_city=next(x for x in cities if x.name == roadLine[1]), cost=int(roadLine[2])))
            elif city.name == roadLine[1]:
                city.roads.append(
                    Road(end_city=next(x for x in cities if x.name == roadLine[0]), cost=int(roadLine[2])))


    # for city in cities:
    #     for road in city.roads:
    #         print(str(city.name) + " " + str(road.endCity.name) + " " + str(road.cost))
