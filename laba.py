import matplotlib.pyplot as plt
import math

allNumbers = [5.69,5.32,5.46,5.52,5.58,5.45,5.38,5.56,5.48,5.34,5.55,5.56,5.38,5.6,5.45,5.52,5.49,5.49,5.68,5.58,5.62,5.52,5.38,5.49,5.47,5.67,5.65,5.47,5.52,5.63,5.57,5.58,5.38,5.4,5.54,5.41,5.7,5.57,5.51,5.58,5.6,5.7,5.6,5.69,5.57,5.57,5.8,5.26,5.73,5.26]
def tArifm():
    # Среднее арифметическое для всех чисел
    sum = 0
    for i in allNumbers: sum += i
    result = sum / len(allNumbers)

    return result
def dispersionNumber():
    # Дисперсия, ширина нормального распределения
    tAr = tArifm()
    sigma = 0
    for i in allNumbers:
        sigma = sigma + (i - tAr)**2
    sigma = (sigma / len(allNumbers))**(1/2)
    #print(sigma)
    return sigma
def gaussFunc(variableT):
    # функция гауссовского распределения
    sigma = dispersionNumber()

    tAr = tArifm()

    gauss3 = (2 * math.pi) ** 0.5
    gauss1 = (1 / (sigma * gauss3))

    gauss4 = (variableT - tAr) ** 2
    gauss5 = 2 * (sigma ** 2)
    gauss2 = math.exp( - (gauss4 / gauss5))

    #print(variableT, gauss1, gauss2, gauss1*gauss2)

    return gauss1*gauss2
def setCellsToTable(*args):
    newList = []
    listsAmount = len(args)
    for i in range(len(args[0])):
        varAr = []
        for j in range(listsAmount):
            element = args[j]
            #print(element)
            #print(type(element), len(element), j, i, listsAmount)

            if type(element[i]) == list:
                #print('problem here1')
                varAr.append(element[i][0])
            else:
                #print('problem here2')
                varAr.append(element[i])
        newList.append(varAr)
    return newList
def deleteHalfOfTheList(currList):
    num = 3
    currList.insert(num, '...')
    for i in range(num+1, len(currList) - num):
        currList.pop(num+1)
    return currList


def FirstTable(shortVersion = False):

    var = [i for i in range(1, len(allNumbers)+1)]

    varAllNumbers = allNumbers

    varT = []
    for i in varAllNumbers:
        print(i, tArifm())
        varT.append(round((i-tArifm()) * 1000) / 1000)

    varT2 = []
    for i in varT: varT2.append(round((i**2) * 1000) / 1000)

    sumN = 0
    for i in varT:
        sumN += i

    if shortVersion:
        var = deleteHalfOfTheList(var)
        varAllNumbers = deleteHalfOfTheList(allNumbers.copy())
        varT = deleteHalfOfTheList(varT)
        varT2 = deleteHalfOfTheList(varT2)


    data = setCellsToTable(var, varAllNumbers, varT, varT2)

    firstCol = ''
    secondCol = '<t> = ' + str(round( (tArifm())*10000 ) / 10000)
    thirdCol = 'Σ(t - <t>) = ' + str(round(sumN * 10000) / 10000)
    fourthCol = 'σ = ' + str(round((dispersionNumber()) * 10000) / 10000)
    fourthCol2 = 'ρ max = ' + str(round((1 / ((2 * math.pi) ** 0.5) / dispersionNumber()) * 10000) / 10000)
    data += [[firstCol, secondCol, thirdCol, fourthCol], ['', '', '', fourthCol2]]

    print(data)
    print(len(data))

    col_labels = ["Номер Опыта", "ti, с", "t - <t>", "(t - <t>)^2"]
    plt.table(cellText=data, colLabels=col_labels, loc='center', colWidths=[0.2,0.25,0.2,0.2])
    #table.scale(1, 2)
    plt.axis("off")
    if shortVersion: plt.savefig(fname="FirstTable-Short.png", bbox_inches='tight', transparent=True)
    else: plt.savefig(fname="FirstTable.jpg", bbox_inches='tight', transparent=True)

    plt.show()
def SecondTable():
    dtNum = 0.07
    allNumbers.sort()
    def numToString(arr):
        newArr = []; N = []
        num = allNumbers[0]
        element = ''
        varN = 0; first = True
        for i in allNumbers:
            if num + dtNum >= i:
                if first: element = str(i); first = False
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

            if i == allNumbers[-1]:
                last = newArr[-1]
                last = str(last)[2:-2]
                last = last[last.rfind(' ') + 1:]
                if i != last:
                    var = [element]
                    print(element)
                    newArr.append(var)
                    N.append(varN)
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
        if len(str(item)) > 8: element = str(round( (gaussFunc(left))*1000 ) / 1000) + '\n' + str(round( (gaussFunc(right))*1000 ) / 1000)
        else: element = str(round( (gaussFunc(right))*1000 ) / 1000)
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
        newArr = []
        N = []
        num = allNumbers[0]
        element = ''
        varN = 0
        first = True
        for i in allNumbers:
            if num + dtNum >= i:
                if first:
                    element = str(i); first = False
                elif varN % 5 == 0:
                    element = element + '\n'
                element = element + '   ' + str(i)
                varN += 1
            else:
                var = [element]
                newArr.append(var)
                N.append(varN)
                varN = 1
                num = i
                element = str(i)

            if i == allNumbers[-1]:
                last = newArr[-1]
                last = str(last)[2:-2]
                last = last[last.rfind(' ') + 1:]
                if i != last:
                    var = [element]
                    newArr.append(var)
                    N.append(varN)

        return (newArr, N)

    var, varN = numToString(allNumbers)
    varNt = []
    for i in range(len(varN)):
        num = varN[i] / len(allNumbers) / dtNum
        num = round(num * 1000) / 1000
        varNt.append(num)
    srValue = []
    val = allNumbers[0]
    res = 0
    num = 0
    widList = []
    for i in allNumbers:
        if val + dtNum >= i:
            res += i
            num += 1
        else:
            srValue.append(round((res / num) * 100) / 100)
            res = i
            num = 1
            val = i

    '''     
    wid = max(allNumbers) - min(allNumbers)
    wid = round(wid / 13 * 1000) / 1000

    #print(max(allNumbers), min(allNumbers), max(allNumbers) - min(allNumbers), (max(allNumbers) - min(allNumbers)) / 8,(max(allNumbers) - min(allNumbers)) / 8 * 1000, wid)
    
    v = min(allNumbers)
    n = []
    for i in range(1, 14):
        v += wid
        v = round(v * 1000) / 1000
        if i % 2 == 1:
            print(v, wid, i)
            n.append(v)
    print(len(n))
    '''
    nm = 7*2
    wid = (5.8 - 5.26) / nm

    val = []
    Num = min(allNumbers)

    for i in range(1, nm):
        Num += wid
        Num = round(Num * 1000) / 1000
        if i % 2 == 1:
            print(Num, wid, i)
            val.append(Num)
    print(len(val))

    varGauss = []
    for i in allNumbers:
        varGauss.append(gaussFunc(i))

    plt.subplot(1, 1, 1)
    plt.plot(allNumbers, varGauss, color='red')

    plt.subplot(1, 1, 1)

    plt.bar(val, varNt, width=2*wid)
    plt.savefig("Gistogram-Gaus Graph.jpg")
    plt.show()
def ThirdTable():

    def In(fromIn, toIn):
        result = 0
        for i in allNumbers:
            if fromIn < i < toIn: result += 1
        return result

    errorNum1 = round(( (round(tArifm() * 1000) / 1000) - (round(dispersionNumber() * 1000) / 1000))*1000)/1000
    errorNum2 = round((round(tArifm() * 1000) / 1000 + 2*round(dispersionNumber() * 1000) / 1000)*1000)/1000
    errorNum3 = round((round(tArifm() * 1000) / 1000 + 3*round(dispersionNumber() * 1000) / 1000)+1000)/1000
    data = [
        ['<t> ± σ ',
         errorNum1, round(tArifm() * 1000) / 1000 + round(dispersionNumber() * 1000) / 1000,
         In(round(tArifm() * 1000) / 1000 - round(dispersionNumber() * 1000) / 1000, round(tArifm() * 1000) / 1000 + round(dispersionNumber() * 1000) / 1000),
         In(round(tArifm() * 1000) / 1000 - round(dispersionNumber() * 1000) / 1000, round(tArifm() * 1000) / 1000 + round(dispersionNumber() * 1000) / 1000)/len(allNumbers),
         0.68
         ],

        ['<t> ± 2σ',
         round(tArifm() * 1000) / 1000 - 2*round(dispersionNumber() * 1000) / 1000, errorNum2,
         In(round(tArifm() * 1000) / 1000 - 2*round(dispersionNumber() * 1000) / 1000, round(tArifm() * 1000) / 1000 + 2*round(dispersionNumber() * 1000) / 1000),
         In(round(tArifm() * 1000) / 1000 - 2 * round(dispersionNumber() * 1000) / 1000, round(tArifm() * 1000) / 1000 + 2 * round(dispersionNumber() * 1000) / 1000)/len(allNumbers),
         0.95
         ],

        ['<t> ± 3σ',
         round(tArifm() * 1000) / 1000 - 3*round(dispersionNumber() * 1000) / 1000, errorNum3,
         In(round(tArifm() * 1000) / 1000 - 3*round(dispersionNumber() * 1000) / 1000, round(tArifm() * 1000) / 1000 + 3*round(dispersionNumber() * 1000) / 1000),
         In(round(tArifm() * 1000) / 1000 - 3*round(dispersionNumber() * 1000) / 1000, round(tArifm() * 1000) / 1000 + 3*round(dispersionNumber() * 1000) / 1000)/len(allNumbers),
         0.997
         ]
    ]
    col_labels = ['', 'Интервал От, с', 'Интервал До, с', 'N 12', 'N 12/n', 'P 12']
    plt.table(cellText=data, colLabels=col_labels, loc='center', colWidths=[0.12, 0.2, 0.2, 0.08, 0.08, 0.08])
    plt.axis("off")
    plt.savefig(fname="ThirdTable.png", bbox_inches='tight', transparent=True)
    plt.show()

