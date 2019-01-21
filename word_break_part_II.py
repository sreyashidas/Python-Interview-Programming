class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def check(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]

    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0:
                print stringlist[1:]
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                print 'i:',i
                if s[:i] in dict:
                    self.dfs(s[i:], dict, stringlist + ' ' + s[:i])

    def wordBreak(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res

obj = Solution()
result = obj.wordBreak('leetcode',['leet','code','lee','cod','t','e'])
print result
