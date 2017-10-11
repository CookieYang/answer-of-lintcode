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

s = Solution()
print(s.twoSum([2,7,11,15],26))
