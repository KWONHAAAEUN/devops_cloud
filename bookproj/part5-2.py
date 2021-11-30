# 리스트의 질문과 답을 차례로 출력
question = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?",
]

answers = ["An exploding sheep.", "No, I'm a frayed knot.", "'Pop!' goes the weasel."]

# 순서대로 출력하는 방법
# for i in range(3):
#     print(question[i])
#     print(answers[i])

# 값을 각각 지정하여 내보내기 위해 튜플의 튜플 방법을 이용했다
q_a = ((0, 1), (1, 2), (2, 0))
for q, a in q_a:
    print("Q:", question[q])
    print("A:", answers[a])
    print()
