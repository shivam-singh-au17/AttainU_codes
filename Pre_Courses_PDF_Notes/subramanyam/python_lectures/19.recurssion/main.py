# If i want Hi to be printed 3 times
# cnt = 0
# def Hello():
#     global cnt
#     if cnt == 3:
#         return
#     print("hi")
#     cnt += 1
#     Hello()

# if __name__ == "__main__":
#     Hello()


# """
# Finding the factorial of a no
# """

# def Factorial(n):
#     """
#     Factorial n will find the factorial of a no n.
#     """
#     if n == 1:
#         return 1

#     fact = n * Factorial(n - 1)
#     return fact

# if __name__ == "__main__":
#     print(Factorial(5))

# def Reverse(str):
#     if str == "":
#         return str

#     rev = str[-1] + Reverse(str[:-1])
#     return rev


# if __name__ == "__main__":
#     print(Reverse("ABCDEF"))


def R(l):
    if len(l) == 0:
        return 0
    count = 0
    if l[-1] % 2 == 0:
        count =  1 + R(l[:-1])
    else:
        count =  R(l[:-1])
    return count


if __name__ == "__main__":
    print(R([12, 22, 32, 43, 58,118, 21]))


def my_recursive_function(n):

     if(n == 0):
        return n
     print(n)
     my_recursive_function(n-1)

my_recursive_function(10)

def fun(c):
    if (c>5):
        return 
    fun(c+1)
    print(c)

fun(1)

def fun(N):
    if (N == 1):
        return 
    print(N)
    fun(N//2)

fun(16)

print()

def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)

print(test(4,7))