prev2 = 0
prev1 = 1

print(prev2)
print(prev1)

for fib in range(10):
    new_fib = prev1 + prev2
    prev2 = prev1
    prev1 = new_fib

print(new_fib)