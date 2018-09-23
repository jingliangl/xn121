#!/usr/bin/env python
# coding=utf-8
from settings import *
from os.path import join, abspath, dirname

# make root path
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

DEBUG = False

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-hans'
LOGIN_URL = "/passport/login/"
LOGIN_REDIRECT_URL = "/passport/"

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.144.151.112',
    'video.weathertj.com',
]

DATABASES = {
}

INSTALLED_APPS += [
    'django_filters',
    'rest_framework',
    'weshow',
]

TV = [
    ('cctv1', '/data/data/tv_json/cctv1.json'),
    ('cctv2', '/data/data/tv_json/cctv2.json'),
    ('cctv4', '/data/data/tv_json/cctv4.json'),
    ('cctv7', '/data/data/tv_json/cctv7.json'),
    ('lyws', '/data/data/tv_json/lyws.json'),
]

EXCEL_DIR = '/data/data/excel/excel'
EXCEL_URL = 'http://video.weathertj.com:8090/data/excel/excel/'
