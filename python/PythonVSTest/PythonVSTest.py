import re
import string
import math

def fibIndexesProgram():
    count = int(input())
    for i in range(0,count):
        current = int(input())
        print(str(fibIndex(current)) + ' ')

def readListByCount():
    inputList = []
    count = int(input())
    for i in input().split():
        inputList.append(float(i))
    return inputList

def smoothingTheWeather():
    temperatures = readListByCount()
    print(temperatures[0])
    for i in range(1,len(temperatures)-1):
        print((temperatures[i-1]+temperatures[i]+temperatures[i+1])/3.0)
    print(temperatures[len(temperatures)-1])

def isPalindrome(s):
    for i in range(0,len(s)):
        if(s[i] != s[len(s) - i - 1]):
            return False
    return True

def palindromesProgram():
    count = int(input())
    for i in range(0,count):
        inputString = re.sub(r'[^\w]','',input()).lower()
        print("Y " if isPalindrome(inputString) else "N ")

def bicycleRaceProgram():
    count = int(input())
    for i in range(0,count):
        distance, speed1, speed2 = (float(s) for s in input().split())
        print(distance / (speed1 + speed2) * speed1, ' ')

def rotateStringProgram():
    count = int(input())
    for i in range(0,count):
        rotation, inputString = input().split()
        rotation = int(rotation)
        print(inputString[rotation:] + inputString[:rotation], ' ')

def josephusProblem(N, K):
    soldiers = list(range(1,N + 1))
    z = 0
    while (len(soldiers) != 1):
        end = len(soldiers)
        i = 0
        while(i < end):
            if(z == K - 1):
                soldiers.remove(soldiers[i])
                end -= 1
            else:
                i += 1
            z = (z + 1) % K
    return soldiers[0]

def josephusProblemProgram():
    N, K = (int(s) for s in input().split())
    print(josephusProblem(N, K))

def pythagoreanTheoremProgram():
    count = int(input())
    for i in range(0,count):
        a,b,c = (int(s) for s in input().split())
        if(a**2 + b**2 > c**2):
            print("A ")
        elif(a**2 + b**2 == c**2):
            print("R ")
        else:
            print("O ")

def squareRootProgram():
    count = int(input())
    for i in range(0,count):
        number, accuracy = (int(s) for s in input().split())
        result = 1.0
        for j in range(0,accuracy):
            result = (result + number / result) / 2
        print(result, ' ')

def dice(num):
    return num % 6 + 1

def caesarShiftProgram():
    count, K = (int(s) for s in input().split())
    for i in range(0,count):
        s = list(input())
        for i in range(0,len(s)):
            if(s[i] >= 'A') and (s[i] <= 'z'):
                s[i] = chr(ord(s[i]) - K);
                if(s[i] < 'A'):
                    s[i] = chr(ord(s[i]) + 26);
        print("".join(s), ' ')

def savingsCalculatorProgram():
    count = int(input())
    for i in range(0, count):
        s, r, p = (int(s) for s in input().split())
        print(math.ceil(math.log(r/s)/math.log(1 + p/100)))

def matchingWordsProgram():
    l = input().split()
    l2 = list()
    for i in range(0, len(l)):
        if (l[i] in l[:i]) and not(l[i] in l2):
            l2.append(l[i])
    l2.sort()
    print(' '.join(l2))

#############################################################################

def normalDistribution(sigma, m, x):
    return math.exp(-(x - m)**2 / (2 * sigma**2)) / (sigma * math.sqrt(2 * math.pi))

#Подсчёт середин интервалов:
def makeAveragesFromIntervals(intervals):
    return [(x + y) / 2 for (x, y) in zip(intervals[:-1], intervals[1:])]

#Получение частот по массиву
def getFrequencies(values):
    return [n / sum([i for i in values]) for n in values]

#n-й момент
def moment(n, values, probabilities):
    return sum([x**n * p for (x, p) in zip(values, probabilities)])

#n-й центральный момент
def centralMoment(n, expectedValue, values, probabilities):
    return moment(n, [(x - expectedValue) for x in values], probabilities)

#Среднее выборочное
def sampleMean(values, probabilities):
    return moment(1, values, probabilities)

def general(value, n):
    return value / n
    
#Дисперсия
def variation(sampleMean, values, probabilities):
    return centralMoment(2, sampleMean, values, probabilities)

#Среднее квадратичное отклонение
def standartDeviation(dispersion):
    return math.sqrt(dispersion)

#Асимметрия
def skewness(sampleMean, standartDeviation, values, probabilities):
    return centralMoment(3, sampleMean, values, probabilities) / standartDeviation ** 3

#Эксцесс
def generalExcess(sampleMean, standartDeviation, values, probabilities, valuesCount):
    return general(centralMoment(4, sampleMean, values, probabilities), valuesCount) / standartDeviation ** 4 - 3



def makeIntervalBorders(x1, step, count):
    intervalBorders = [x1]
    for i in range(1,count):
        intervalBorders.append(intervalBorders[i-1] + step)
    return intervalBorders

def readInt(string):
    print("Введите " + string + ": ", end="")
    return int(input())

def probabilityTheoryHomework():
    #intervalBorders = [ 6, 16, 26, 36, 46, 56, 66, 76, 86 ]
    #counts = [ 8, 7, 16, 35, 15, 8, 6, 5 ]

    #Концы интервалов:
    intervalBorders = [ 6, 10, 14, 18, 22, 26, 30, 34, 38, 42 ]
    #Значения интервалов:
    counts = [ 15, 26, 25, 30, 26, 21, 24, 20, 13 ]

    #Ввод:
    x1 = readInt("x1")
    step = readInt("шаг")
    count = readInt("количество")
    counts = []
    for i in range(1, count):
        counts.append(readInt("n" + str(i)))

    intervalBorders = makeIntervalBorders(x1, step, count)
    values = makeAveragesFromIntervals(intervalBorders)
    frequencies = getFrequencies(counts) #Считаем частоты
    n = sum(counts) #Число опытов
    #Получаем необходимые параметры:
    sampleMean = sampleMean(values, frequencies)
    variation = variation(sampleMean, values, frequencies)
    standartDeviation = standartDeviation(variation)
    skewness = skewness(sampleMean, standartDeviation, values, frequencies)
    excess = centralMoment(4, sampleMean, values, frequencies) / standartDeviation ** 4 - 3

    #Вывод:
    print("Средние значения: ", " ".join(str(x) for x in values))
    print("Частоты: ", " ".join(str(x) for x in frequencies))
    print("Выборочное среднее: ", sampleMean)
    print("Дисперсия: ", variation)
    print("Среднее квадратичное отклонение: ", standartDeviation)
    print("Асимметрия: ", skewness)
    print("Эксцесс: ", excess)

#############################################################################



def triangleArea():
    count = int(input())
    for i in range(0,count):
        x1, y1, x2, y2, x3, y3 = (int(s) for s in input().split())
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
        print(area, ' ')

def rockPaperScissors():
    count = int(input())
    winningMap = { "R" : "S", "S" : "P", "P" : "R" }
    for i in range(0,count):
        ranks = "RPS"
        matches = input().split()
        playerPoints = [0, 0]
        for match in matches:
            if(match[0] == match[1]):
                continue
            if(winningMap[match[0]] == match[1]):
                playerPoints[0] += 1
            else:
                playerPoints[1] += 1
        print(1 if playerPoints[0] > playerPoints[1] else 2, ' ')

def matchingBrackets():
    count = int(input())
    openingBrackets = "({[<"
    closingBrackets = ")}]>"
    for i in range(0,count):
        right = True
        bracketsStack = []
        inputString = input()
        for char in inputString:
            if char in openingBrackets:
                bracketsStack.append(char)
            elif (char in closingBrackets) and ((len(bracketsStack) == 0) \
                or (char != closingBrackets[openingBrackets.find(bracketsStack.pop())])):
                right = False
                break
        if(len(bracketsStack) > 0):
            right = False
        print(1 if right else 0, end=' ')

def cards():
    count = int(input())
    suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    for word in input().split():
        cardIndex = int(word)
        suitIndex = int(cardIndex / 13)
        rankIndex = cardIndex % 13
        print(ranks[rankIndex] + '-of-' + suits[suitIndex] + ' ')

def foolsDay2014():
    count = int(input())
    for test in range(0,count):
        sum = 0
        for word in input().split():
            sum += int(word)**2
        print(sum, end=' ')

def bullsAndCows():
    secret, guessNum = input().split()
    for guess in input().split():
        bulls, cows = 0, 0
        for i in range(0,4):
            if (guess[i] == secret[i]):
                bulls += 1
            elif (guess[i] in secret):
                cows += 1
        print(str(bulls) + '-' + str(cows), end=' ')

def combinationCounting():
    count = int(input())
    for i in range(0,count):
        N, K = (int(word) for word in input().split())
        C = int(math.factorial(N) / (math.factorial(K) * math.factorial(N - K)))
        print(C, end=' ')

def f(A, B, C, D, x):
    return A * x + B * math.pow(x, 1.5) - C * math.exp(-x / 50) - D

def binarySearch():
    count = int(input())
    for i in range(0,count):
        A, B, C, D = (float(word) for word in input().split())
        a, b, precision = 0, 100, 0.0000001
        while (b - a > precision):
            c = (a + b) / 2
            if(f(A, B, C, D, a) * f(A, B, C, D, c) < 0):
                b = c
            elif(f(A, B, C, D, a) * f(A, B, C, D, c) > 0):
                a = c
            else:
                a = c
                break
        print(a, end=' ')

def selectionSort():
    count = int(input())
    array = list(int(word) for word in input().split())
    for i in range(0,count - 1):
        max = 0
        for j in range(1,count - i):
            if(array[j] > array[max]):
                max = j
        print(max, end=' ')
        array[max], array[count - i - 1] = array[count - i - 1], array[max]

def quadraticEquation():
    count = int(input())
    for case in range(0, count):
        A, B, C = (int(word) for word in input().split())
        D = B**2 - 4 * A * C
        if(D >= 0):
            x1 = int((-B + math.sqrt(D)) / (2 * A))
            x2 = int((-B - math.sqrt(D)) / (2 * A))
            print(x1, x2, end='')
        else:
            real = int(-B / (2 * A))
            imaginary = int(math.sqrt(abs(D)) / (2 * A))
            print(real, '+', imaginary, 'i ', real, '-', imaginary, 'i', sep='', end='')
        if(case < count - 1):
            print('; ')

def compare(a,b):
	ret = a,b
	if(a>b):
		ret = b,a
	return ret

def greatestCommonDivisor(a,b):
	a,b = compare(a,b)
	while (a%b!=0):
		a,b = b,a%b
	return b

def leastCommonMultiple(a,b):
	return a*b/greatestCommonDivisor(a,b)

def twoPrinters():
    count = int(input())
    for case in range(0,count):
        X, Y, N = (int(word) for word in input().split())
        if(X > Y):
            X, Y = Y, X
        totalX, totalY = 0, 0
        lcm = int(leastCommonMultiple(X, Y))
        lcmN = int(lcm / X + lcm / Y)
        lcmCount = int(N / lcmN)
        total = lcm * lcmCount
        for page in range(lcmCount * lcmN,N):
            if((totalX + X <= totalY + Y) or (totalX <= totalY)):
                totalX += X
            else:
                totalY += Y
        print(total + max(totalX, totalY), end = ' ')

def blackjack():
    count = int(input())
    ranks = {"T" : 10, "J" : 10, "Q" : 10, "K" : 10}
    for case in range(0,count):
        sum = 0
        aces = 0
        for word in input().split():
            if(word >= "0" and word <= "9"):
                sum += int(word)
            elif(word == "A"):
                aces += 1
            else:
                sum += ranks[word]
        while(aces > 0):
            if(11 - sum >= aces):
                sum += 11
            else:
                sum += 1
            aces -= 1
        print(sum if sum <= 21 else "Bust", end=' ')

def kingAndQueen():
    count = int(input())
    for case in range(0,count):
        king, queen = input().split()
        kingX = ord(king[0]) - ord('a') + 1
        kingY = int(king[1])
        queenX = ord(queen[0]) - ord('a') + 1
        queenY = int(queen[1])
        if(kingX == queenX or kingY == queenY 
           or kingX + kingY == queenX + queenY
           or kingX - kingY == queenX - queenY):
            print("Y", end=' ')
        else:
            print("N", end=' ')

def cardShuffling():
    deck = []
    for suit in "CDHS":
        for value in "A23456789TJQK":
            deck.append(suit + value)
    i = 0
    for random in input().split():
        j = int(random) % 52
        deck[i], deck[j] = deck[j], deck[i]
        i += 1
    print(' '.join(deck))



def LinearCongruentialGenerator(A, C, M, x0, N):
    randomNumbers = []
    for j in range(0, N):
        x0 = (A * x0 + C) % M
        randomNumbers.append(x0)
    return randomNumbers, x0;

def fibIndex(end):
	if(end <= 1):
		return end
	current = 1
	previous = 0
	index = 1
	while(current < end):
		current, previous = previous, current
		current += previous
		index += 1
	return index

def funnyWordsGenerator():
    letters = ["bcdfghjklmnprstvwxz", "aeiou"]
    count, x0 = (int(word) for word in input().split())
    lengthes = (int(word) for word in input().split())
    for length in lengthes:
        randomValues, x0 = LinearCongruentialGenerator(445, 700001, 2097152, x0, length)
        for i in range(0,length):
            print(letters[i % 2][randomValues[i] % len(letters[i % 2])], end='')
        print(' ',end='')

def fibonacciDivisibility():
    count = int(input())
    for M in (int(word) for word in input().split()):
        current = 1
        previous = 0
        index = 1
        while(current % M != 0):
            current, previous = previous, current
            current += previous
            index += 1
        print(index, end=' ')

def mortgageCalculator():
    P, R, L = (int(word) for word in input().split())
    R = R / 12 / 100
    M = math.ceil(P * (R * pow(R + 1, L)) / (pow(R + 1, L) - 1))
    print(M)

def checkTicTacToeWin(turns):
    wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win in wins:
       i = 0
       for num in win:
           if(num in turns):
               i += 1
       if(i == 3):
           return True
    return False

def ticTacToe():
    count = int(input())
    for case in range(0,count):
        players = [[], []]
        firstPlayer = True
        win = False
        turnNum = 1
        for turn in (int(word) for word in input().split()):
            i = int(not(firstPlayer))
            players[i].append(turn)
            if(checkTicTacToeWin(players[i])):
                print(turnNum, end=' ')
                win = True
                break
            firstPlayer = not(firstPlayer)
            turnNum += 1
        if(not(win)):
            print(0, end=' ')




def prime(n):
    for x in range(2,int(math.sqrt(n) + 1)):
        if n%x==0:
            return x
    else:
        return 0

def primeText(n):
    result = 1
    p = prime(n)
    if(p):
        while(p):
            result += 1
            n=n//p
            p = prime(n)
    return result

def olymp():
    num = int(input())
    if(primeText(num) == 20):
        print("Yes")
    else:
        print("No")
    #primeText(32)

def someShit():
    count = int(input())
    array = list(int(word) for word in input().split())
    for i in range(1,len(array)):
        swapCount = 0
        while(array[i] < array[i - 1]):
            array[i], array[i - 1] = array[i - 1], array[i]
            swapCount += 1
        print(swapCount,end=' ')
    print(array)

import math

def someShit2():
    count = int(input())
    for case in range(0,count):
        A, B = (int(x) for x in input().split())
        print(math.floor(math.sqrt(B)) - math.ceil(math.sqrt(A)) + 1)


def contiguousSum(array):
    size = len(array)
    if(size <= 1):
        return array[0]
    sums = [sum(array)]
    for i in range(2):
        subarraySum = sum(array[i:(size - 1 + i)])
        if(subarraySum > sums[0]):
            sums.append(contiguousSum(array[i:(size - 1 + i)]))
    return max(sums)

def maxSum(array):
    size = len(array)
    if(size <= 1):
        return array[0]
    return max(sum(array), maxSum(array[:(size-1)]), maxSum(array[1:]))

def positiveSum(array):
    sum = 0
    nonNegative = False
    for i in array:
        if(i >= 0):
            sum += i
            nonNegative = True
    return (sum if nonNegative else max(array))

def someShit():
    count = int(input())
    for case in range(count):
        input()
        array = list(int(i) for i in input().split())
        print(maxSum(array), positiveSum(array))

def numa(s, n):
    res = 0
    for c in s[:n]:
        if(c == 'a'):
            res += 1
    return res

def brute(l, n):
    for i in range(n-3,-1,-1):
        for j in range(n-2,i,-1):
            for k in range(n-1,j,-1):
                if(l[i]+l[j]>l[k] and l[i]+l[k]>l[j] and l[j]+l[k]>l[i]):
                    return [l[i],l[j],l[k]]
    return [-1]
def hz():
    n = int(input().strip())
    ss = []
    for i in range(0,n):
        ss.append(input().strip())
    for s in ss:
        s = list(s)
        for i in range(len(s)-2,-1,-1):
            if(s[i] < max(s[i+1:])):
                j = s.index(min([c for c in s[i+1:] if c > s[i]]))
                s[i], s[j] = s[j], s[i]
                s[i+1:] = sorted(s[i+1:])
                print(''.join(s))
                break
        else:
            print("no answer")

print("I'm working!")