class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countingSort():
            minVal, maxVal = min(nums), max(nums)
            count = [0] * (maxVal - minVal + 1)
            for num in nums:
                count[num - minVal] += 1
            
            index = 0
            for val, freq in enumerate(count):
                while freq > 0:
                    nums[index] = val + minVal
                    index += 1
                    freq -= 1

        countingSort()
        return nums