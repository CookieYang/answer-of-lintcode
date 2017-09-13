def anagrams(strs):
    def generateLabel(s):
        tmp = [0]*26
        label = ''
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            tmp[index] += 1
        for i in range(26):
            if tmp[i] != 0:
                label += chr(i + ord('a')) + str(tmp[i])
        return label
    dic = {}
    result = []
    for i in range(len(strs)):
        label = generateLabel(strs[i])
        if label in dic.keys():
            dic.get(label).append(strs[i])
        else:
            dic[label] = [strs[i]]
    for j in dic.keys():
        if len(dic[j]) > 1:
            result.extend(dic[j])
    return result





c = anagrams(["lint","intl","inlt","code",'deoc'])
print(c)