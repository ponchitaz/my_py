x = input('The first word: ')
y = input('The second word: ')

def howFar(x,y):
    theX = len(x)
    theY = len(y)
    if theX > theY:
        x, y = y, x
        theX, theY = theY, theX

