# list
# 항상 좌항과 우항의 개수가 같아야함
# *__에 남은 값 저장 ex) *extra
name, age, region = ["Tom", 10, "Seoul"]

name, *__ = ["Tom", 10, "Seoul"]

__, age, __ = ["Tom", 10, "Seoul"]
