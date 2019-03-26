from django.db import models


class Post(models.Model):
    title = models.CharField("제목", max_length=50)
    contents = models.CharField("내용", max_length=50)
