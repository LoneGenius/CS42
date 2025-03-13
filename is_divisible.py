def square(x):
    return x * x 
print(square(5))

def sum_squares(x,y):
    return add(square(x), square(y))
print(square(3))

def g(h, i):
    return h + i
print(g(1, 2))  # Output: 3

from math import pi
tau = 2 * pi
print(pi)
print(tau)

from operator import mul
def square(x):
    return mul(x,x)
print(mul(100,3))
print(square(4))

f = max  # Save the built-in max function
result = f(2, 3, 4)  # Finds the max value → 4
print(result)  # Output: 4

# Don't overwrite max
# max = 3  ❌ This would break the code

print(max(1, 4))  # Output: 4

del max  # Deletes the integer `3` and restores built-in `max`
print(max(1, 4))  # Works again

