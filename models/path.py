class Path:
    def __init__(self, current_city, visited_cities, distance_progress, priority):
        self.currentCity = current_city
        self.visitedCities = [] if visited_cities is None else visited_cities
        self.distanceProgress = distance_progress
        self.priority = priority

    def toString(self):
        return "Path(currentCity: " + str(self.currentCity.name) + ", visitedCities: " \
               + str([CITY.name for CITY in self.visitedCities]) + ", distanceProgress: " + str(
            self.distanceProgress) + ")"

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority
