class NumericLists:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(0, len(nums)):
            n1 = nums[i]
            complement = target - n1
            if complement in h:
                return [i, h[complement]]
            else:
                h[n1] = i