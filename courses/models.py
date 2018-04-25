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
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "courseinfo"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="lesson")
    name = models.CharField(max_length=100, verbose_name="chaptername")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="video")
    name = models.CharField(max_length=100, verbose_name="videoname")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name="courseresource")
    name = models.CharField(max_length=100, verbose_name="sourcername")
    download = models.FileField(max_length=100,upload_to="course/%Y/%m",verbose_name="resource")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "courseresource"
        verbose_name_plural = verbose_name