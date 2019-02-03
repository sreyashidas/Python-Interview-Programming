class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 
        j = len(numbers) - 1
        
        while i < j :
            x = numbers[i] + numbers[j]
            if x < target:
                i= i + 1
            elif x > target:
                j = j - 1
            else:
                return [i+1,j+1]
