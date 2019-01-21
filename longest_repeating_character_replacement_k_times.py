import collections
def characterReplacement( s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    '''
    Sliding Window + Counter

        For a window whose size is W, and the char with max occurance has max_cnt, then
    the operations needed at least are (W - max_cnt).
        Because we are looking for the max sized window, we don't have to shrink start pointer
    until the window becomes valid again.
        A trick part of this solution is that, although the max_cnt could be invalid at some point,
    it doesn't matter because:
    1. if later there is a higher max_cnt, the windows size will be kept which is valid before.
    2. if later there isn't a higher max_cnt, the windows will be updated so as the max_cnt.
    '''
    max_dup = 0
    cntr = collections.defaultdict(int)
    print cntr
    left = 0
    for right, c in enumerate(s):
        cntr[c] += 1
        if cntr[c] > max_dup:
            max_dup = cntr[c]
        width = right - left + 1
        print 'width: ', width, ' left: ',left,' right: ', right, 'cntr: ', cntr, 'c: ', c, 'max dup: ', max_dup
        if width - max_dup > k:
            print 'Eureka'
            lc = s[left]
            cntr[lc] -= 1
            left += 1
            print left,'left:right', right
    print len(s), left
    return len(s) - left


result = characterReplacement ('AABABBA',1)
print result
