def calculate_pi():
    result = 0
    sign = 1
    denominator = 1
    pi = 0

    while round(pi, 6) != 3.141593:
        result += sign * (1 / denominator)
        pi = result * 4
        sign *= -1
        denominator += 2

    return round(pi, 6)