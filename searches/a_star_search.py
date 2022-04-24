from queue import PriorityQueue

from models.path import Path


def a_star_search(cities, start, end):
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
                         priority=path.distanceProgress + road.endCity.straightLineDistance))
    return Path(None, [], 0, 0)
