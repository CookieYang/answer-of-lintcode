def previousPermuation(nums):
    change_index = -1
    # 找到需要变换的比后一个数字大的数
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] < nums[i - 1]:
            change_index = i - 1
            break
    if change_index == -1:
        nums.reverse()
        return nums
    min_nums_index = change_index + 1
    # 找到后面列表中比change_index元素小的最大值
    for j in range(change_index + 1, len(nums)):
        if (nums[j] < nums[change_index]) and (nums[min_nums_index] < nums[j]):
            min_nums_index = j
    # 交换元素
    nums[change_index], nums[min_nums_index] = nums[min_nums_index], nums[change_index]
    # 排序后面的列表，降序
    back = sorted(nums[change_index + 1:], reverse=True)
    nums[change_index + 1:] = back
    return nums