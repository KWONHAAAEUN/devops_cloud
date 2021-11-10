def get_counts(s):
    count = 0
    for ch in s:
        if ch != " ":
            count += 1
    return count


print(get_counts("우리는 파이썬을 즐겨요"))
