# an English submarine 이름은 Boaty McBoatface로 지어졌다
# an Australian 이름은 Horsey McHorseface로 지어졌다
# a Swedish train 이름은 Trainy McTrainface로 지어졌다
# 문자열 'duck', 'gourd', 'spitz'과 %포매팅을 사용하여 출력하기

names = ["duck", "gourd", "spitz"]

for name in names:
    cap_names = name.capitalize()
    print("%sy Mc%sface" % (cap_names, cap_names))

# format 메서드 사용
print("{}y Mc{}face".format(cap_names, cap_names))
# f-문자열 사용
print(f"{cap_names}y Mc{cap_names}face")
