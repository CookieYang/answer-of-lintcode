def mergeSortedArray(A, B):
    lA = len(A) - 1
    lB = len(B) - 1
    i = 0
    j = 0
    newArr = []
    while i <= lA and j <= lB:
        if A[i] <= B[j]:
            newArr.append(A[i])
            i += 1
        else:
            newArr.append(B[j])
            j += 1

    while j <= lB:
        newArr.append(B[j])
        j += 1

    while i <= lA:
        newArr.append(A[i])
        i += 1
    return newArr

def mergeSortedArray2(A,m,B,n):
    pos = m + n - 1
    posA = m - 1
    posB = n - 1
    while posA >= 0 and posB >= 0 :
        if A[posA] > B[posB] :
            A[pos] = A[posA]
            pos -= 1
            posA -= 1
        else:
            A[pos] = B[posB]
            pos -= 1
            posB -= 1

    while posA >= 0 :
        A[pos] = A[posA]
        pos -= 1
        posA -= 1
    while posB >= 0 :
        A[pos] = B[posB]
        pos -= 1
        posB -= 1
