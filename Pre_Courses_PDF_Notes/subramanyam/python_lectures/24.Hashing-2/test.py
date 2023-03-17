
# a = [2, 1, 7, 4, 6, 8, 1, 9]

# count = 0
# stask = []
# i = 0
# temp = a[i]
# while i < len(a):
#     if a[i] > temp:
#         count = count + 1

#         if count == 1:
#             stask.append(a[i])
#         else:
#             count = 0
#             i = i + 1
#     i = i + 1
# print(stask)

# # TODO:




def firstMaxNumStore(A):

    myStack = []
    maxElmt = [0] * len(A)

    for idx, val in enumerate(A):

        if len(myStack) == 0:
            myStack.append(idx)
        else:
            cur = val
            while len(myStack) != 0 and A[myStack[-1]] < cur:

                x = myStack[-1]
                myStack.pop()
                maxElmt[x] = cur
            myStack.append(idx)
    
    while len(myStack) != 0:
        
        x = myStack[-1]
        myStack.pop()
        maxElmt[x] = None
        
    return maxElmt



if __name__ == "__main__":
    A = [2, 1, 7, 4, 6, 8, 1, 9]
    
    ans = firstMaxNumStore(A)
    print(ans)