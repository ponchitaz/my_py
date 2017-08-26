import random

theText = input('Tell me a story: ')
theWords = theText.split()

def shuffledText(singleWord):
    singleWord = list(singleWord)
    random.shuffle(singleWord)
    singleWord = ''.join(singleWord)
    return singleWord

def main():
    for singleWord in theWords:
        if len(singleWord) > 3:
            if singleWord[-1] == ",":
                print(singleWord[0] + '' + shuffledText(singleWord[1:-2]) + '' + singleWord[-2::], end=" ")
            else:
                print(singleWord[0] + '' + shuffledText(singleWord[1:-1]) + '' + singleWord[-1], end=" ")
        else:
            print(singleWord, end=" ")

main()