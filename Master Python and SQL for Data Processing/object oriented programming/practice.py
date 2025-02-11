class MaxNumberFinder:
    def __init__(self, nums):
        self.nums:list[int] = nums

    def find_max_number(self):
        if not self.nums:
            return None
        return max(self.nums)
        
finder = MaxNumberFinder([1,3,4,2])
finder.find_max_number()