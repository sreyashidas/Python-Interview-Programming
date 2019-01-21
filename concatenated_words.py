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
                if ' ' in stringlist[1:]:
                    Solution.res.append(stringlist.split(' '))

            for i in range(1, len(s) + 1):
                print 'i:',i
                if s[:i] in dict:
                    self.dfs(s[i:], dict, stringlist + ' ' + s[:i])

    def concatenatedWords(self, strList, dict):
        Solution.res = []
        Solution.final = set()
        for i in strList:
            self.dfs(i, dict, '')

            for i in Solution.res:
                Solution.final.add(''.join(i))

        return Solution.final

obj = Solution()
result = obj.concatenatedWords(['leetcode','leet','code'],['leet','code'])
print result
