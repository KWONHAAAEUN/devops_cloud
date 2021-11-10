# 교육 7일차

## 파이썬 map

목록으로부터 값을 하나씩 받아서 변환하여, 
새로운 목록을 생성

```python
def make_power(number):
    return number ** 2
for number in map(make_power,range(1,10))
    print(number)
```