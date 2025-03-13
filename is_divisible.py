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

if 21 % 3 == 0:
    print("21 is divisible by 3")
else:
    print("21 is not divisible by 3")

num = int(input("Enter a number: "))
divisor = int(input("Enter a divisor: "))

if num % divisor == 0:
    print(f"{num} is divisible by {divisor}")
else:
    print(f"{num} is not divisible by {divisor}")
    
def is_divisible(num, divisor):
    return num % divisor == 0

assert is_divisible(25, 5) is True
assert is_divisible(26, 5) is False


assert is_divisible(10, 2) is True, 
assert is_divisible(10, 3) is False, 
assert is_divisible(21, 7) is True, 
assert is_divisible(15, 4) is False, 
assert is_divisible(0, 5) is True, 




