def removeKey(self, counters):
    keySet = counters.keys()
    removeList = []
    for key in keySet:
        counters[key] -= 1
        if counters[key] == 0:
            removeList.append(key)

    for key in removeList:
        counters.pop(key, None)


def majorityNumber(self, nums, k):
    counters = {}
    for num in nums:
        if num not in counters:
            counters[num] = 1
        else:
            counters[num] += 1

        if len(counters) >= k:
            self.removeKey(counters)

    if len(counters) == 0:
        return -1

    # 从新计算剩下的数字中在原数组的出现次数
    for key in counters.keys():
        counters[key] = 0

    for num in nums:
        if num in counters:
            counters[num] += 1

    # find the max key
    maxCounter, maxKey = 0, 0
    for key, value in counters.iteritems():
        if value > maxCounter:
            maxCounter = value
            maxKey = key

    return maxKey
