from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="org_list"),  # org list
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)$', OrgHomeView.as_view(), name='home_view'),
]
