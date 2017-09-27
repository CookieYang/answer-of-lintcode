from structs import MyNode

class Solution:
    def countOfSmallerNumberII(self, A):
        res = [0] * len(A)
        root = MyNode(A[0])
        for i in range(1,len(A)):
            tmp = root
            count = 0
            while True:
                if tmp.data > A[i]:
                    tmp.l_count += 1
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = MyNode(A[i])
                        break
                elif tmp.data < A[i]:
                    count += tmp.l_count + tmp.rep
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = MyNode(A[i])
                        break
                else:
                    count += tmp.l_count
                    tmp.rep += 1
                    break
            res[i] = count
        return res


solution = Solution()
print(solution.countOfSmallerNumberII([1,2,7,8,5]))

