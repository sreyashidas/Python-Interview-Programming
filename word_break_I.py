def wordBreak(s, dict):
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(1, len(s)+1):
        for k in range(i):
            print i, k, s[k:i]
            if dp[k] and s[k:i] in dict:
                dp[i] = True
                print 'Eureka'

        print dp
    return dp[len(s)]

result = wordBreak('leetcode',['lee','leet','code','cod','t','e'])
print result
