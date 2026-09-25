def calculate_digits_sum(number):
    totalSum=0

    while number > 0:
        totalSum += number % 10
        number //= 10

    print(f"Sum of digits: {totalSum}")

calculate_digits_sum(123456789)
calculate_digits_sum(112233445566778899)
calculate_digits_sum(123456789 * 987654321)

