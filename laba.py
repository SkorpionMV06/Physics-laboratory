import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import math
allNumbers = [5.69,5.32,5.46,5.52,5.58,5.48,5.34,5.55,5.56,5.38,5.6,5.45,5.52,5.49,5.49,5.68,5.58,5.62,5.52,5.38,5.49,5.47,5.67,5.65,5.47,5.52,5.63,5.57,5.58,5.38,5.4,5.54,5.41,5.7,5.57,5.51,5.58,5.6,5.7,5.6,5.69,5.57,5.57,5.8,5.26,5.73,5.26]
allNumbers.sort()
def tArifm():
    # Среднее арифметическое для всех чисел
    sum = 0
    for i in allNumbers: sum += i

    return sum / len(allNumbers)
def dispersionNumber():
    # Дисперсия, ширина нормального распределения
    tAr = tArifm()
    teta = 0
    for i in allNumbers:
        teta = teta + (i - tAr)**2
    teta = (teta / 50)**(1/2)
    #print(teta)
    return teta
def gaussFunc(t):
    # функция гауссовского распределения
    gauss = 0
    teta = dispersionNumber()
    tAr = tArifm()
    gauss = (1 / (teta * ((2*(math.pi))**0.5)))  *  math.exp( - ( (t - tAr)**2 ) / (2 * teta*teta))
    return gauss
def setCellsToTable(*args):
    newList = []
    listsAmount = len(args)
    for i in range(len(args[0])):
        varAr = []
        for j in range(listsAmount):
            if type(args[j][i]) == list: varAr.append(args[j][i][0])
            else: varAr.append(args[j][i])
        newList.append(varAr)
    return newList
def deleteHalfOfTheList(currList):
    num = round(len(currList)/10)
    currList.insert(num, '...')
    print(num, len)
    for i in range(num+1, len(currList) - num): currList.pop(num+1)
    return currList


def FirstTable():
    var = []
    for i in range(1, 48): var.append(i)
    var = deleteHalfOfTheList(var)
    varAllNumbers = deleteHalfOfTheList(allNumbers)
    data = setCellsToTable(var, varAllNumbers)


    col_labels = ["Номер Опыта", "ti, с"]
    plt.table(cellText=data, colLabels=col_labels, loc='center', colWidths=[0.27, 0.15])
    plt.axis("off")
    plt.savefig(fname="FirstTable.png", bbox_inches='tight', transparent=True)

    plt.show()
def SecondTable():
    dtNum = 0.07
    allNumbers.sort()
    def numToString(arr):
        newArr = []; N = []
        num = allNumbers[0]
        element = ''
        varN = 0; f = True
        for i in allNumbers:
            if num + dtNum >= i:
                if f: element = str(i); f = False
                elif varN % 5 == 0: element = element + '\n'
                element = element + '   ' + str(i)
                varN += 1
            else:
                var = []; var.append(element)
                newArr.append(var)
                N.append(varN)
                varN = 1
                num = i
                element = str(i)


        return (newArr, N)

    var, varN = numToString(allNumbers)
    varNt = []
    varP = []
    for i in range(len(varN)):
        num = round( (varN[i]/len(allNumbers)/dtNum)*1000 ) / 1000
        varNt.append(num)
    for item in var:
        left = item[0]
        right = item[0]

        left = left[:left.find(' ')]
        right = right[right.rfind(' ')+1:]

        left = float(left)
        right = float(right)

        element = ''
        element = str(round( (gaussFunc(left))*1000 ) / 1000) + '\n' + str(round( (gaussFunc(right))*1000 ) / 1000)
        varP.append(element)


    data = setCellsToTable(var, varN, varNt, varP)
    col_labels = ["Границы интервалов, с", "ΔN", "ΔN/NΔt, c^-1", "ρ, c^-1"]
    table = plt.table(colLabels=col_labels, cellText=data, loc='center', colWidths=[0.4, 0.085, 0.18, 0.15])
    table.scale(1, 3)
    plt.axis("off")
    plt.savefig(fname="SecondTable.png", bbox_inches='tight', transparent=True)
    plt.show()
def GausGraph():
    dtNum = 0.07
    allNumbers.sort()

    def numToString(arr):
        newArr = [];
        N = []
        num = allNumbers[0]
        element = ''
        varN = 0;
        f = True
        for i in allNumbers:
            if num + dtNum >= i:
                if f:
                    element = str(i); f = False
                elif varN % 5 == 0:
                    element = element + '\n'
                element = element + '   ' + str(i)
                varN += 1
            else:
                var = [];
                var.append(element)
                newArr.append(var)
                N.append(varN)
                varN = 1
                num = i
                element = str(i)

        return (newArr, N)

    var, varN = numToString(allNumbers)
    varNt = []
    varP = []
    for i in range(len(varN)):
        num = round((varN[i] / len(allNumbers) / dtNum) * 1000) / 1000
        varNt.append(num)
    srValue = []
    val = allNumbers[0];
    res = 0;
    num = 0
    for i in allNumbers:
        if val + dtNum >= i:
            res += i;
            num += 1
        else:
            srValue.append(round((res / num) * 100) / 100)
            res = i;
            num = 1;
            val = i
    print(varNt, srValue)

    v = 5.26;
    n = []
    for i in range(6):
        v += 0.067
        v = round(v * 1000) / 1000
        n.append(v)

    varGauss = []
    for i in allNumbers:
        varGauss.append(gaussFunc(i))

    plt.subplot(1, 1, 1)
    plt.plot(allNumbers, varGauss, color='red')

    plt.subplot(1, 1, 1)
    # [5.339,5.,5.418,5.497,5.576,5.655]
    plt.bar(n, varNt, width=0.067)
    plt.savefig("Gistogram-Gaus Graph.png")
    plt.show()
def ThirdTable():

    return

FirstTable()