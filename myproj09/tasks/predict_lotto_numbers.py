import random


def check_available(received_text: str) -> bool:
    return received_text in ("로또", "로또번호 정지해줘")


def make_response(received_text: str, candidate_numbers: list[int]) -> str:
    if candidate_numbers is None:
        candidate_numbers = random.sample(range(1, 46), 7)
    *numbers, bonus = candidate_numbers
    predict_numbers: str = ",".join(map(sorted(numbers)))
    message = f"로또 번호는 {predict_numbers} 이며 보너스 번호는 {bonus}입니다"
    return message
