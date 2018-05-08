from datetime import datetime
from django.db import models


# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="cityname")
    add_time = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=200, verbose_name="description")

    class Meta:
        verbose_name = "city"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="orgname")
    desc = models.TextField(verbose_name="description")
    click_num = models.IntegerField(default=0, verbose_name="clicknumber")
    fav_num = models.IntegerField(default=0, verbose_name="savenum")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="figure", max_length=100)
    address = models.CharField(max_length=150, verbose_name="address")
    city = models.ForeignKey(CityDict, verbose_name="incity")
    add_time = models.DateTimeField(default=datetime.now)
    category = models.CharField(default="pxjg",max_length=20,verbose_name="orgname", choices=(
    ("pxjg", "Traning Organization"), ("school", "School"), ("Individual", "Individual")))

    class Meta:
        verbose_name = "courseorg"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="inorg")
    name = models.CharField(max_length=10, verbose_name="teachername")
    work_years = models.IntegerField(default=0, verbose_name="workyear")
    work_company = models.CharField(max_length=50, verbose_name="companyrname")
    work_position = models.CharField(max_length=50, verbose_name="position")
    points = models.CharField(max_length=50, verbose_name="strenght")
    click_num = models.IntegerField(default=0, verbose_name="clicknumber")
    fav_num = models.IntegerField(default=0, verbose_name="savenum")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = verbose_name
