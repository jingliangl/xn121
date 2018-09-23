# coding=utf-8

from django.conf.urls import url, include
from rest_framework import routers
from weshow.api import WeshowView
from excel.api import ExcelView

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/weshow/', WeshowView.as_view()),
    url(r'^api/excel/', ExcelView.as_view()),
]
