from test04 import make_powerd_list, make_powerd_list2

# 이 테스트가 이 함수에 대한 스팩
def test_make_powerd_list():
    numbers = [0, 1, 2, 3, 4]
    excepted = [0, 1, 4, 9, 16]
    assert make_powerd_list(numbers) == excepted


def test_make_powerd_list2():
    numbers = [0, 1, 2, 3, 4]
    excepted = [0, 1, 4, 9, 16]
    assert make_powerd_list2(numbers) == excepted
