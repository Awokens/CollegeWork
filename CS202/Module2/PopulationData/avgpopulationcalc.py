def readData(filePath):
    with open(filePath, 'r') as file:
        populationData = [int(line.strip()) for line in file]
    return populationData

def calculateAvgChange(populationData):
    totalChange = 0
    for i in range(1, len(populationData)):
        change = populationData[i] - populationData[i-1]
        totalChange += change
    averageChange = totalChange / (len(populationData) - 1)
    return averageChange

def findYearWithMaxIncrease(populationData):
    maxIncrease = 0
    maxIncreaseYear = 0
    for i in range(1, len(populationData)):
        increase = populationData[i] - populationData[i-1]
        if increase > maxIncrease:
            maxIncrease = increase
            maxIncreaseYear = i + 1950
    return maxIncreaseYear

def findYearWithMinIncrease(populationData):
    minIncrease = float('inf')
    minIncreaseYear = 0
    for i in range(1, len(populationData)):
        increase = populationData[i] - populationData[i-1]
        if increase < minIncrease:
            minIncrease = increase
            minIncreaseYear = i + 1950
    return minIncreaseYear

def main():
    filePath = 'CS202/Module2/PopulationData/USPopulation.txt'
    populationData = readData(filePath)
    averageChange = calculateAvgChange(populationData)
    yearWithMaxIncrease = findYearWithMaxIncrease(populationData)
    yearWithMinIncrease = findYearWithMinIncrease(populationData)

    print(f"Average annual change in population: {averageChange}")
    print(f"Year with the greatest increase in population: {yearWithMaxIncrease}")
    print(f"Year with the smallest increase in population: {yearWithMinIncrease}")

if __name__ == '__main__':
    main()