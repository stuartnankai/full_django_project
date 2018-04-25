from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=10, verbose_name="nickname", default="")
    birthday = models.DateField(verbose_name="birthday", null=True, blank=True)
    gender = models.CharField(choices=(("male", "male"), ("female", "female")), default="male", max_length=10)
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=12, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png")

    class Meta:
        verbose_name = "userinfo"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="verifycode")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(max_length=20, choices=(("register", "register"), ("forget", "getpassword")))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "emailverify"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="banner", max_length=100)
    url = models.URLField(max_length=200, verbose_name="visiturl")
    index = models.IntegerField(default=100, verbose_name="order")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addtime")

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = verbose_name
