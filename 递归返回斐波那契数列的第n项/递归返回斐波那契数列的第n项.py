n = eval(input("Please input a Number:"))
def Finbonacci(n):
    if n<=1:
        return n
    else:
        return Finbonacci(n-1)+Finbonacci(n-2)
print(Finbonacci(n))