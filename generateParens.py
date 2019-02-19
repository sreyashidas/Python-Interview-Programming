def generateParens(n):
    chosen = []
    openB = 0
    closeB = 0
    generateParensHelper(openB, closeB, n, chosen)


def generateParensHelper(openB, closeB, n, chosen):
    print 'generateParensHelper', openB, closeB, n, chosen
    if closeB == n:
        print ''.join(chosen)
    else:
        if openB > closeB:
            chosen.append(')')
            generateParensHelper(openB, closeB+1, n, chosen)
            chosen.pop()

        if openB < n:
            chosen.append('(')
            generateParensHelper(openB+1, closeB, n, chosen)
            chosen.pop()


generateParens(2)
