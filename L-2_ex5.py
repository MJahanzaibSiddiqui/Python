

import cmath


class Calculator0:
    def __pow__(self, a, b):
        self.a = a
        return a ** b


# Create an instance of the Calculator class
calculator = Calculator0()

num1 = complex(input("Enter first number (in the form a+bj): "))
num2 = complex(input("Enter second number (in the form a+bj): "))

# Call the power method through the instance
result0 = calculator.__pow__(num1, num2)

print(f"{num1} power {num2} = {result0}")


# ------------------------------------------------------------------------

class Calculator1:
    def __add__(self, x, y):
        self.x = x
        return x + y


# Create an instance of the Calculator class
calculator = Calculator1()

num3 = complex(input("Enter first number (in the form a+bj): "))
num4 = complex(input("Enter second number (in the form a+bj): "))

# Call the add method through the instance
result1 = calculator.__add__(num3, num4)

print(f"{num3} addition {num4} = {result1}")


# ------------------------------------------------------------------------

class Calculator2:
    def __truediv__(self, p, q):
        self.p = p
        return p / q


# Create an instance of the Calculator class
calculator = Calculator2()

num7 = complex(input("Enter first number (in the form a+bj): "))
num8 = complex(input("Enter second number (in the form a+bj): "))

# Call the divide method through the instance
result2 = calculator.__truediv__(num7, num8)

print(f"{num7} divide {num8} = {result2}")

# ------------------------------------------------------------------------


class Calculator3:
    def __sub__(self, m, n):
        self.m = m
        return m - n


# Create an instance of the Calculator class
c = Calculator3()

num5 = complex(input("Enter first number (in the form a+bj): "))
num6 = complex(input("Enter second number (in the form a+bj): "))

# Call the sub method through the instance
result3 = c.__sub__(num5, num6)
print(f"{num5} sub {num6} = {result3}")


# ------------------------------------------------------------------------

# Input complex numbers
num5 = complex(input("Enter first number (in the form a+bj): "))
# Calculate and display the conjugates
conjugate_num5 = num5.conjugate()
print(f"Conjugate of {num5} is {conjugate_num5}")


# ------------------------------------------------------------------------


# Input a complex number
num = complex(input("Enter a complex number (in the form a+bj): "))

# Calculate the polar angle (theta) in radians
theta = cmath.phase(num)

print(f"Polar angle (theta) of {num}: {theta} radians")
