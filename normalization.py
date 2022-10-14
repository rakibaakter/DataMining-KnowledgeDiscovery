import math

#min max normalization
def minMax(data, rangeMin, rangeMax):
    normalizezData = []
    min = data[0]
    max = data[len(data) - 1]

    for i in range(len(data)):
        normalizezData.append(((data[i] - min) / (max - min)) * (rangeMax - rangeMin) + rangeMin)
    return normalizezData
# z score
def std_deviation(data, mean):
    xi = 0
    sumX = 0
    for val in data:
        xi = val - mean
        sqrXi = math.pow(xi,2)
        sumX += sqrXi
    return math.sqrt(sumX/len(data))
def z_Scrore(data):
    mean = 0
    sumZ = 0
    # stdDeviation = 0
    for val in data:
        sumZ += val
    mean = sumZ/len(data)
    stdDeviation = std_deviation(data, mean)
    #print(stdDeviation)
    normalizezDataZ = []

    for i in range(len(data)):
        normalizezDataZ.append((data[i] - mean) / stdDeviation)
    return normalizezDataZ

def decimalScaling(data):
    normalizezDataD = []
    j = len(str(max(data)))
    for i in range(len(data)):
        normalizezDataD.append(data[i] / math.pow(10,j))
    return normalizezDataD



data = [8, 10, 15, 20]
data.sort()
print("min max normalization")
normalizezData = minMax(data, 0, 1)
for i in range(len(normalizezData)):
    print(data[i], "=", "{:.5f}".format(normalizezData[i]))
print("z score normalization")
normalizezData = z_Scrore(data)
for i in range(len(normalizezData)):
    print(data[i], "=", "{:.5f}".format(normalizezData[i]))
print("decimal scaling normalization")
normalizezData = decimalScaling(data)
for i in range(len(normalizezData)):
    print(data[i], "=", "{:.5f}".format(normalizezData[i]))


