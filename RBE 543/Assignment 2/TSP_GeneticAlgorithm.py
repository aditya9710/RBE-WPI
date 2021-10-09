import random
import copy
import math
import matplotlib.pyplot as plt

# Initialization
populationSize = 20
citySize = 20
tourSize = 21
numExecution = 10_000
population = []
x = []
y = []

tour = [[0 for x in range(tourSize)] for y in range(tourSize)]
dCidade = [[0 for x in range(populationSize)] for y in range(populationSize)]
distances = [0 for x in range(populationSize)]
parentsOne = None
parentsTwo = None
costByExecution = []

"""Generate Population"""


def generateFirstPopulation():
    # For each position generate a new possible path
    for i in range(1, populationSize + 1):
        generatePossiblePath()


"""Generate New Possible Path"""


def generatePossiblePath():
    path = []
    for _ in range(1, citySize + 1):
        # Genetate a new number between 1 to citySize
        randomCity = random.randint(1, populationSize)
        # while the number exists in the list, generate a new number
        while (numberExistsInPath(path, randomCity)):
            randomCity = random.randint(1, populationSize)
        path.append(randomCity)
    population.append(path)


"""Method to verify if city is already in path"""


def numberExistsInPath(path, city):
    for i in path:
        if i == city:
            return True
    return False


"""Generate X & Y arrays which represent the distance in x & y axes
    These are used to calculate the Identity Matrix in the fitness function"""


def generateXandY():
    for _ in range(citySize):
        randomCity = random.random()
        randomCity = round(randomCity, 2)
        x.append(randomCity)

        randomCity = random.random()
        randomCity = round(randomCity, 2)
        y.append(randomCity)


"""Generates the tour matrix, same as the population but with the first column
duplicated at the end, since the traveler always arrives back at the initial
city"""


def generateTour():
    global tour
    tour = copy.deepcopy(population)
    for ways in tour:
        first = ways[0]
        ways.append(first)


"""Generate an array with the sum of rach path in the population array 
based on the tour matrix"""


def calculateDistance():
    global distances
    distances = [0 for x in range(citySize)]
    for i in range(len(population)):
        for j in range(len(population[i])):
            firstPosition = citySize - 1 if tour[i][j] == citySize else tour[i][j]
            secondPosition = citySize - 1 if tour[i][j + 1] == citySize else tour[i][j + 1]
            distances[i] += round(dCidade[firstPosition][secondPosition], 4)
    dict_distance = {i: distances[i] for i in range(0, len(distances))}
    distances = copy.deepcopy(dict_distance)
    return sorted(distances.items(), key=lambda kv: kv[1])


"""Generate the identity matric (dCidade) based on x and y arrays
and then call calculateDistance() to generate array with the sum of each path
"""


def fitnessFuction():
    for i in range(len(population)):
        for j in range(len(population)):
            dCidade[i][j] = round(math.sqrt(((x[i] - x[j]) ** 2) + ((y[i] - y[j]) ** 2)), 4)
    return calculateDistance()


"""Performs the rouletteWheel function, generating two arrays with 5 parents each"""


def rouletteWheel(sortedX):
    global parentsOne
    global parentsTwo
    arr = []
    rouletteArr = []
    for i in range(round(populationSize/2)):
        arr.append(sortedX[i][0])

    for j in range(len(arr)):
        for _ in range(round(populationSize/2) - j):
            rouletteArr.append(arr[j])

    parentsOne = createParents(rouletteArr)
    parentsTwo = createParents(rouletteArr)


"""Auxillary funciton in rouletteWheel() to generate two parent arrays"""


def createParents(rouletteArr):
    parentsArr = []
    for _ in range(5):
        parentsArr.append(rouletteArr[random.randint(0, 54)])
    return parentsArr


"""Swaps two cities in path with 5% chance of mutation"""


def mutate(matrix):
    for i in range(len(matrix)):
        for _ in range(len(matrix[i])):
            randomNumber = random.randint(1, 100)
            if randomNumber >= 1 and randomNumber <= 5:
                indexOne = random.randint(0, citySize - 1)
                indexTwo = random.randint(0, citySize - 1)
                auxOne = matrix[i][indexOne]
                auxTwo = matrix[i][indexTwo]
                matrix[i][indexOne] = auxTwo
                matrix[i][indexTwo] = auxOne


def doCycle(sortedX):
    global population
    children = []

    for i in range(5):
        parentOneAux = parentsOne[i]
        parentTwoAux = parentsTwo[i]
        usedIndices = []

        randomIndexInsideCromosome = random.randint(0, populationSize - 1)

        usedIndices.append(randomIndexInsideCromosome)

        childOne = copy.deepcopy(population[parentOneAux])
        childTwo = copy.deepcopy(population[parentTwoAux])

        valAuxOne = childOne[randomIndexInsideCromosome]
        valAuxTwo = childTwo[randomIndexInsideCromosome]

        childOne[randomIndexInsideCromosome] = valAuxTwo
        childTwo[randomIndexInsideCromosome] = valAuxOne

        while(hasDuplicity(childOne, usedIndices) != -1):
            newIndex = hasDuplicity(childOne, usedIndices)
            usedIndices.append(newIndex)

            valAuxOne = childOne[newIndex]
            valAuxTwo = childTwo[newIndex]

            childOne[newIndex] = valAuxTwo
            childTwo[newIndex] = valAuxOne


        # After generating, add them to the children array
        children.append(childOne)
        children.append(childTwo)

    mutate(children)

    tempPop = copy.deepcopy(population)

    for i in range(10):
        population[i] = copy.deepcopy(tempPop[sortedX[i][0]])

    for j in range(10, populationSize):
        population[j] = copy.deepcopy(children[j - 10])


def hasDuplicity(auxArray, usedIndices):
    for i in range(len(auxArray)):
        for j in range(i, len(auxArray)):
            if i != j and auxArray[i]  == auxArray[j]:
                if i in usedIndices:
                    return j
                else:
                    return i
    return -1


def main():
    generateFirstPopulation()
    generateXandY()
    generateTour()

    for _ in range(numExecution):
        sortedX = fitnessFuction()
        rouletteWheel(sortedX)
        doCycle(sortedX)
        generateTour()
        costByExecution.append(sortedX[0][1])

    sortedX = fitnessFuction()

    print('Total Population: %s' %(populationSize))
    print('Mutation Probability 5%')
    print('Number of cities: %s' %(citySize))
    print('Optimal path cost: %s' %(sortedX[0][1]))
    print('Best Route: %s' %(population[0]))

    plt.plot(tour[0])
    plt.plot(tour[0], 'ro')
    plt.axis([0, 20, 0, 20])
    plt.show()

    plt.plot(costByExecution)
    plt.show()


if __name__ == '__main__':
    main()