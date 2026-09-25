# def 통해서 9,10,11 넣으면 값 구하고 2,3,4,5 거듭제곱 구하는 것 구하기

def calculate_powers(max):
    totalSum = 0

    for i in range(1, max+1):
        totalSum += int("1" * i)

    print(f"{max}'s sum: {totalSum}")

    for i in range(2, 6):
        power = totalSum ** i
        print(f"{totalSum}^{i} = {power}")

calculate_powers(9)
calculate_powers(10)
calculate_powers(11)