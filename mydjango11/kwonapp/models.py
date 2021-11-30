from django.db import models


class profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    gen = (
        ("남", "남"),
        ("여", "여"),
    )
    gender = models.CharField(
        max_length=2, choices=gen, verbose_name="성별", default=""
    )  # 장고는 choicefield를 사용할 수 없어서 choice 옵션을 추가하여 사용
    pub_date = models.DateField(verbose_name="생일")
    address = models.CharField(max_length=100, verbose_name="주소")
    mobile = models.CharField(max_length=13, verbose_name="연락처")
