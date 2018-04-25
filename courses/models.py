from datetime import datetime


from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="coursename")
    desc = models.CharField(max_length=300, verbose_name="description")
    detail = models.TextField(verbose_name="detail")
    degree = models.CharField(max_length=5, choices=(("easy", "easy"), ("middle", "middle"), ("hard", "hard")))
    learn_time = models.IntegerField(default=0, verbose_name="learningtime")
    students = models.IntegerField(default=0, verbose_name="numberofstudent")
    fav_num = models.IntegerField(default=0, verbose_name="savenumber")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="figure", max_length=100)
    click_num = models.IntegerField(default=0, verbose_name="clicknum")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="addtime")

    class Meta:
        verbose_name = "courseinfo"
        verbose_name_plural = verbose_name
