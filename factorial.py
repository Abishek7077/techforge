def factorial_num(n):
    result= 1
    for i in range(1,n+1):
        result *= i
    return result
    
print(factorial_num(5))

# n = int(input())

# factorial = 1

# for i in range(1,n+1):
#     factorial *= i

# print(factorial)