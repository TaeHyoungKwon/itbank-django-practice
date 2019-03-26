from django.db import models


class HouseKeepingBook(models.Model):
    contents = models.CharField("내용", max_length=200, blank=True)
    income = models.IntegerField("수입", null=True, default=0)
    expense = models.IntegerField("지출", null=True, default=0)
    count = models.IntegerField("개수", null=True, default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.contents)
