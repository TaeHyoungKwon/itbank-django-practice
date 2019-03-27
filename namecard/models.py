from django.db import models
from django.shortcuts import reverse


class NameCard(models.Model):
    company = models.CharField("회사명", max_length=100)
    name = models.CharField("이름", max_length=50)
    comp_part = models.CharField("부서", max_length=50)
    position = models.CharField("직위", max_length=25)
    age = models.IntegerField("나이")
    gender = models.CharField("성별", max_length=10)
    phone = models.CharField("핸드폰 번호", max_length=25)
    comp_number = models.CharField("사무실 번호", max_length=25)
    fax_number = models.CharField("Fax 번호", max_length=25)
    create_date = models.DateField("등록일", auto_now_add=True)
    remark = models.TextField("설명")

    def __str__(self):
        return str(name) + " " + str(company)

    def get_absolute_url(self):
        return reverse("namecard:detail", kwargs={"id": self.pk})
