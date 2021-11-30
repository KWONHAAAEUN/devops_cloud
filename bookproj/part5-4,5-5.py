# 문장에 format 사용하여 문자를 넣어 출력해보기

letter = """
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that in should never be used in a {room},
especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another{product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}
"""

print(
    letter.format(
        salutation="권",
        name="하은",
        product="제품",
        verbed="버브",
        room="방",
        animals="동물",
        amount="수량",
        percent="퍼센트",
        spokesman="대변인",
        job_title="회사명",
    )
)
