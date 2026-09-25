import math

def challenge(max):
    answer = math.lcm(*range(1, max + 1))
    print(f"The smallest positive number divisible by all integers from 1 to {max} is: {answer}")

challenge(20)
challenge(200)
challenge(2000)






