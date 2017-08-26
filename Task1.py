import random

theText = input('Tell me a story: ')
theWords = theText.split()

class letsShuffle(object):

    def shuffledText(self, singleWord):
        singleWord = list(singleWord)
        random.shuffle(singleWord)
        singleWord = ''.join(singleWord)
        print(singleWord)

    def main(self, singleWord):
        for singleWord in theWords:
            if len(singleWord) > 3:
                if singleWord[-1] == ",":
                    print(singleWord[0] + ''.join(random.sample(singleWord[1:-2],  len(singleWord)-3)) + '' + singleWord[-2::], end=" ")
                else:
                    print(singleWord[0] + ''.join(random.sample(singleWord[1:-1], len(singleWord)-2)) + '' + singleWord[-1], end=" ")
            else:
                print(singleWord, end=" ")

letsShuffle().main(theText)

