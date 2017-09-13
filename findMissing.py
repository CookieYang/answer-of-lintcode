def helpFind(str,numList,depth,n):
    l = len(str)
    if depth > l - 1:
        return True
    if depth == l - 1:
        n1 = int(str[depth])
        if n1 == 0 or n1 in numList:
            return False
        else:
            numList.append(n1)
            return True
    else:
        n1 = int(str[depth])
        n2 = int(str[depth+1])
        if n1 == 0:
            return False
        if n1 in numList:
            if n1*10 + n2 in numList or n1*10 + n2 > n:
                return False
            else:
                numList.append(n1*10+n2)
                if helpFind(str,numList,depth+2,n):
                    return True
                else:
                    numList.pop()
                    return False
        else:
            numList.append(n1)
            if helpFind(str,numList,depth+1,n):
                return True
            else:
                numList.pop()
                if n1*10 + n2 in numList or n1*10 + n2 > n:
                    return False
                else:
                    numList.append(n1 * 10 + n2)
                    if helpFind(str, numList, depth + 2,n):
                        return True
                    else:
                        numList.pop()
                        return False

def findMissing2(n, str):
    list = []
    helpFind(str,list,0, n)
    print(list)
    return int((1 + n)*n / 2 - sum(list))
print(findMissing2(13,'1110987654321213'))