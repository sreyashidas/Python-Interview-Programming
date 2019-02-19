def combinationSum(digits, desiredSum):
    chosen = []
    combinationSumHelper(digits, chosen, 0,  desiredSum)

def combinationSumHelper(digits, chosen, sumSoFar, desiredSum):
    print 'combinationSumHelper ', 'digits=',digits, 'chosen=',chosen, 'sumSoFar=',sumSoFar, 'desiredSum=',desiredSum
    if sumSoFar == desiredSum:
        print chosen
        return

    if sumSoFar > desiredSum:
        return

    for i in range(len(digits)):
    	c = digits[i]
        # choose
        chosen.append(c)

        #explore
        combinationSumHelper(digits, chosen, sumSoFar + c, desiredSum )

        #un-choose
        chosen.remove(c)

combinationSum([2,3,6,7],8)
