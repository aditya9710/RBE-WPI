import random


def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution


def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength


def getNeighbors(solution):
    neighbors = []

    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)

    return neighbors


def getBestNeighbor(tsp, neighbors):
    bestRouteLength = routeLength(tsp, neighbors[0])
    bestNeighbor = neighbors[0]

    for neighbor in neighbors:
        currentRouteLength = routeLength(tsp, neighbor)

        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbor = neighbor

    return bestNeighbor, bestRouteLength


def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    print(currentSolution)
    currentRouteLength = routeLength(tsp, currentSolution)
    print(currentRouteLength)
    neighbors = getNeighbors(currentSolution)
    print(neighbors)
    bestNeighbor, bestNeighbourRouteLength = getBestNeighbor(tsp, neighbors)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbor
        currentRouteLength = bestNeighbourRouteLength
        neighbors = getNeighbors(currentSolution)
        bestNeighbor, bestNeighbourRouteLength = getBestNeighbor(tsp, neighbors)

    return currentSolution, currentRouteLength

def main():
    tsp = [[0, 400, 500, 300],
           [400, 0, 300, 500],
           [500, 300, 0, 400],
           [300, 500, 400, 0]]

    print(hillClimbing(tsp))


if __name__ == "__main__":
    main()
