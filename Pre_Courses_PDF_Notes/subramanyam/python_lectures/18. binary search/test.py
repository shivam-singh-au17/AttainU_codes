
A = [2]

def peak(A):
    n = len(A)

    for i in range(0, n):
        if i ==0 and A[i+1] < A[i]:
            return i
        if i == n-1 and A[i-1]< A[i]:
            return i
        if A[i] > A[i-1] and A[i] > A[i+1]:
            return i

print(peak(A))