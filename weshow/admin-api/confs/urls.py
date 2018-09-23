# coding=utf-8

from django.conf.urls import url, include
from rest_framework import routers
from weshow.api import WeshowView

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^api/', include(router.urls)),
    # admin, search
    url(r'^api/weshow/', WeshowView.as_view()),
]
