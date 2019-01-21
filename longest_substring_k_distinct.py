def lengthOfLongestSubstringKDistinct( s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = {}
    pt = 0
    max_len = 0

    for i, c in enumerate(s):
        count[c] = i
        if (len(count) > k):
            pt = min(count.values())
            del count[s[pt]]
            pt += 1
        max_len = max(max_len, i - pt + 1)
        print 'i: ',i, ' c: ', c , ' count: ', count, ' maxlen: ', max_len, 'pt: ', pt ,' i - pt + 1 : ' , i - pt + 1

    return max_len

result = lengthOfLongestSubstringKDistinct('abcbbbbcccbdddadacb',2)
print result
