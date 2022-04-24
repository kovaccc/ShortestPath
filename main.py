from queue import PriorityQueue


class Road:
    def __init__(self, end_city, cost):
        self.endCity = end_city
        self.cost = cost

    def toString(self):
        return "Road(endCity: " + str(self.endCity.toString()) + ", cost: " \
               + str(self.cost) + ")"


class City:
    def __init__(self, name, straight_line_distance):
        self.name = name
        self.straightLineDistance = straight_line_distance
        self.roads = []

    def toString(self):
        return "City(name: " + str(self.name) + ", straightLineDistance: " \
               + str(self.straightLineDistance) + ", roads: " + str(self.roads) + ")"


class Path:
    def __init__(self, current_city, visited_cities, distance_progress, priority):
        self.currentCity = current_city
        self.visitedCities = [] if visited_cities is None else visited_cities
        self.distanceProgress = distance_progress
        self.priority = priority

    def toString(self):
        return "Path(currentCity: " + str(self.currentCity.name) + ", visitedCities: " \
               + str([CITY.name for CITY in self.visitedCities]) + ", distanceProgress: " + str(
            self.distanceProgress) + ") "

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority


def greedy_best_first_search(cities, start, end):
    priority_queue = PriorityQueue()
    start_city = cities[cities.index(next(x for x in cities if x.name == start))]
    priority_queue.put(Path(current_city=start_city, visited_cities=[], distance_progress=0, priority=0))

    while priority_queue.not_empty:
        path = priority_queue.get()
        if path.currentCity.name == end:
            return path
        for road in path.currentCity.roads:
            if road.endCity not in path.visitedCities:
                priority_queue.put(
                    Path(current_city=road.endCity,
                         visited_cities=path.visitedCities + [path.currentCity],
                         distance_progress=path.distanceProgress + road.cost,
                         priority=road.endCity.straightLineDistance))


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

    print(greedy_best_first_search(cities, "Malaga", "Valladolid").toString())
    # for city in cities:
    #     for road in city.roads:
    #         print(str(city.name) + " " + str(road.endCity.name) + " " + str(road.cost))
