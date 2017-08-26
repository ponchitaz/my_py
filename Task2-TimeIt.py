import timeit
import distance

def howFar(x,y):
    theX = len(x)
    theY = len(y)

    if theX > theY:
        x, y = y, x
        theX, theY = theY, theX

    activeLine = range(theX+1)
    print(activeLine)

    for i in range(1, theY+1):
        previousLine = activeLine
        activeLine = [i] + [0] * theX

        for j in range(1, theX+1):
            addSymbol = previousLine[j]+1
            deleteSymbol =activeLine[j-1]+1
            changeSymbol =previousLine[j-1]

            if x[j-1] != y[i-1]:
                changeSymbol += 1
            activeLine[j] = min(addSymbol, deleteSymbol, changeSymbol)

    return activeLine[theX]

# firstSt = input('The first word: ')
# secondSt = input('The second word: ')

firstSt = "mini"
secondSt = "mono"

# проверка истинности утверждения в отладочных целях
assert howFar(firstSt, secondSt) == distance.levenshtein(firstSt, secondSt)

# проверяем время исполнения для обоих алгоритмов
print(timeit.timeit('howFar("mini", "mono")',

                    # "__...__" - указание на приватность атрибута
                    # - привет, инкапсуляция!
                    setup = "from __main__ import howFar",

                    # количество повторений основного выражения;
                    number = 1))
print(timeit.timeit('distance.levenshtein("mini", "mono")',
                    setup = "import distance",
                    number = 1))