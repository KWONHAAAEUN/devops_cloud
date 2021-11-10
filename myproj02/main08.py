def calculate_sum(max_number):
    accumulator = 0  # 누적
    for i in range(1, max_number + 1):
        accumulator = accumulator + i
    return accumulator


print(calculate_sum(100))
