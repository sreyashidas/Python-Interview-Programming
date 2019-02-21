import collections

def findLadders(beginWord, endWord, wordList):

    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = collections.defaultdict(list)
        print 'layer=', layer
        for w in layer:
            print 'w=', w
            if w == endWord:
                print 'inside w == endWord'
                res.extend(k for k in layer[w])
                print res
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i]+c+w[i+1:]
                        print 'neww=', neww
                        if neww in wordList:
                            print 'inside neww in wordList'
                            print 'layer=', layer
                            newlayer[neww]+=[j+[neww] for j in layer[w]]
                            print 'newlayer=', newlayer
        print 'here', set(newlayer.keys())

        wordList -= set(newlayer.keys())
        layer = newlayer

    return res


D = []
D.append("hot")
D.append("dot")
D.append("dog")
D.append("lot")
D.append("log")
D.append("cog")
start = "hit"
target = "cog"
print findLadders(start, target, D)
