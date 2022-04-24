from searches.a_star_search import a_star_search
from models.city import City
from searches.greedy_search import greedy_best_first_search
from models.road import Road

with open('resources/Assignment 1 Spain map.txt') as knapsackFile:
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

    print("Greedy best-first search: \n" + greedy_best_first_search(cities, "Malaga", "Valladolid").toString())
    print("A* search: \n" + a_star_search(cities, "Malaga", "Valladolid").toString())
