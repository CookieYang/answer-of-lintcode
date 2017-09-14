def findDuplicate(nums):
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    find = 0
    while find != slow:
        slow = nums[slow]
        find = nums[find]
    return find
