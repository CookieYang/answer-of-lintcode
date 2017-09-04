def heapify(A):
    for i in range(len(A)):
        while A[i] < A[int((i-1)/2)] and i != 0:
            A[i], A[int((i-1)/2)] = A[int((i-1)/2)], A[i]
            i = int((i-1)/2)
    return A

print(heapify([3,7,5,9,2]))