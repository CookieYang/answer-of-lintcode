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

    print(generateLabel('aacczzz'))



anagrams('a')