# # -------*** factorial ***------- #
def factorial(n):
 s = n
 for i in range(1, n):
    s = s * i
 return s


num = int(input("Enter number to find fcatorial! "))
result = factorial(num)
print("Factorial of "+str(num)+" is",result)

# # ----****-----
# # -----*** fabonacci ***---- #
def fabonacci(j):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(1, j-1):
        rslt = n1 + n2
        n1 = n2
        n2 = rslt
        print(n2)


j = int(input("enter number till which you want to generate series"))
fabonacci(j)
