import time 

def calculate_power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

input_num1 = int(input("Enter base: "))
input_num2 = int(input("Enter exp: "))

start = time.time()
answer = calculate_power(input_num1, input_num2)
end = time.time()

print(f"Result: {answer}")
print(f"It takes {end-start} seconds")