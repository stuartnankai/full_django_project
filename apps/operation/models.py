from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="username")
    mobile = models.CharField(max_length=12, verbose_name="phonenum")
    course_name = models.CharField(max_length=50, verbose_name="coursename")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "userask"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    # course comments
    user = models.ForeignKey(UserProfile, verbose_name="user")
    course = models.ForeignKey(Course, verbose_name="course")
    comments = models.CharField(max_length=200, verbose_name="comment")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "coursecomment"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="user")
    fav_id = models.IntegerField(default=0, verbose_name="dataid")
    fav_type = models.IntegerField(choices=(("1", "course"), ("2", "org"), ("3", "teacher")), default=1,
                                   verbose_name="fav_type")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "userfav"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="receiveuser")
    message = models.CharField(max_length=500, verbose_name="message")
    has_read = models.BooleanField(default=False, verbose_name="isread")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "usermessage"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="user")
    course = models.ForeignKey(Course, verbose_name="course")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "usercourse"
        verbose_name_plural = verbose_name
