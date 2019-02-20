# To check if strings differ by
# exactly one character

def isadjacent(a, b):
    count = 0
    n = len(a)

    # Iterate through all characters and return false
    # if there are more than one mismatching characters
    for i in range(n):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            break

    return True if count == 1 else False


# A queue item to store word and minimum chain length
# to reach the word.
class QItem():

    def __init__(self, word, len):
        self.word = word
        self.len = len


# Returns length of shortest chain to reach
# 'target' from 'start' using minimum number
# of adjacent moves.  D is dictionary
def shortestChainLen(start, target, D):
    # Create a queue for BFS and insert
    # 'start' as source vertex
    Q = []
    item = QItem(start, 1)
    Q.append(item)

    while (len(Q) > 0):

        curr = Q.pop()
        print 'curr=',curr.word
        # Go through all words of dictionary
        print '### start=',start,'target=',target,'D=',D
        for it in D:
            print '### Dictionary=',D
            print 'item from D=',it

            # Process a dictionary word if it is
            # adjacent to current word (or vertex) of BFS
            temp = it
            if isadjacent(curr.word, temp) == True:

                print '->isadjacent'

                # Add the dictionary word to Q
                item.word = temp
                item.len = curr.len + 1
                Q.append(item)
                print 'Q=',Q[0].word

                # Remove from dictionary so that this
                # word is not processed again.  This is
                # like marking visited
                D.remove(temp)

                # If we reached target
                if temp == target:
                    print '->isTarget'
                    return item.len
            else:
                print '->notAdjacent'


D = []
D.append("poon")
D.append("plee")
D.append("same")
D.append("poie")
D.append("plie")
D.append("poin")
D.append("plea")
start = "toon"
target = "plea"
print "Length of shortest chain is: %d" \
      % shortestChainLen(start, target, D)










start = 'toon'  # Add to queue
target = 'plea'
D = ['poon', 'plee', 'same', 'poie', 'plie', 'poin', 'plea']
Q = [(toon,1)]

item = poon # Add to queue
Q = [(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'poin', 'plea']

item = plee # No changes
Q = [(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'poin', 'plea']

item = same # No changes
Q = [(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'poin', 'plea']

item = poie # No changes
Q = [(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'poin', 'plea']

item = plie # No changes
Q = [(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'poin', 'plea']

item = poin # Add to queue
Q = [(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'plea']

item = plee # No changes
Q = [(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'plea']

item = same # No changes
Q = [(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'poie', 'plie', 'plea']

item = poie # Add to queue
Q = [(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'plie', 'plea']

item = plee # No changes
Q = [(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'plie', 'plea']

item = same # No changes
Q = [(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'plie', 'plea']

item = plie # Add to queue
Q = [(plie,4),(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['plee', 'same', 'plea']

item = plee # Add to queue
Q = [(plee,5),(plie,4),(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['same', 'plea']

item = same # No changes
Q = [(plee,5),(plie,4),(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['same', 'plea']

item = plea # No changes
Q = [(plea,7)(,plee,6),(plie,5),(poie,4),(poin,3),(poon,2),(toon,1)]
D = ['same']
