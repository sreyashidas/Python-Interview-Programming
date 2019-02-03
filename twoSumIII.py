class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(int)
        
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.lookup[number] +=  1
        
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        lookup1 = self.lookup
        for i, num in enumerate (lookup1):
            target = value - num
            if target != num and target in lookup1 or target == num and lookup1[num] > 1:
                return True
        return False
            

# Your TwoSum object will be instantiated and called as such:

s = TwoSum()
s.add(2)
s.add(7)

print (s.find(9))
