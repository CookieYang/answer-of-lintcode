class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        m = len(num1)
        n = len(num2)
        i = m - 1
        j = n - 1
        flag = 0
        while i >=0 or j >= 0:
            a = int(num1[i]) if i >=0 else 0
            i = i - 1
            b = int(num2[j]) if j >=0 else 0
            j = j - 1
            sum = a + b + flag
            res = str(sum % 10 ) + res;
            flag = sum / 10
        return res if flag == 0 else (str(flag)+ res)