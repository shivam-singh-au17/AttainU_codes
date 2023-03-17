"""
Given 2 arrays sorted arrays A and B. 
We need to merge them and get sorted Array C.
A = [1, 4, 6, 7, 8, 9]
B = [3, 5, 14, 18]
C = [1, 3, 4, 5, 6, 7, 8, 9, 14, 18]
"""


def Merge2SortedArray(A, B):
    C = []
    for x in A:
        C.append(x)

    for x in B:
        C.append(x)

    C.sort() # O(Nlogn)
    return C


# O(n) time complexity


def Merge2SortedArray2(A, B):
    n = len(A)
    m = len(B)

    p1 = 0
    p2 = 0

    C = list()

    while p1 < n and p2 < m:
        if A[p1] < B[p2]:
            C.append(A[p1])
            p1 += 1
        else:
            C.append(B[p2])
            p2 += 1

    while p1 < n:
        C.append(A[p1])
        p1 += 1

    while p2 < m:
        C.append(B[p2])
        p2 += 1

    return C






def merge(nums1, m, nums2, n):

	last = m + n - 1
	i, j = m - 1, n -1
    
	while last >= 0:
		if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
			nums1[last] = nums1[i]
			i -= 1
		else:
			nums1[last] = nums2[j]
			j -= 1
		last -= 1
	return nums1