class Solution:
    def twoSum(self, numbers, target):
        table = {}
        list = []
        for i in range(len(numbers)):
            key = target - numbers[i]
            if numbers[i] in table.keys():
                list.append(table[numbers[i]])
                list.append(i)
                break
            else:
                table[key] = i
        return list

    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res

    def fourSum(self, nums, target):
        # write your code here
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res

    def threeSumClosest(self, numbers, target):
        numbers.sort()
        ans = None
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            while l < r :
                sum = numbers[i] + numbers[l] + numbers[r]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    l += 1
                else:
                    r -= 1
        return ans


s = Solution()
num = [2,-1,4,3]
s.threeSum(num)
print(num)
