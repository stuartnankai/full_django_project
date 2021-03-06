"""full_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwd, ResetView, ModifyPwdView
from organization.views import OrgView
from full_web_app.settings import MEDIA_ROOT

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>\.*)/$', ActiveUserView.as_view(), name="user_active"),  # pick the parameters
    url(r'^forget/$', ForgetPwd.as_view(), name="forget_pwd"),  # forget pwd
    url(r'^reset/(?P<reset_code>\d+)/$', ResetView.as_view(), name="reset_pwd"),  # pick the parameters
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modeify_pwd"),  # change pwd

    # course org setup
    url(r'^org/', include('organization.urls',namespace="org")),
    # show the image
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT})

]
