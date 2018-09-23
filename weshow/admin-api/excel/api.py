# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, time
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class ExcelView(APIView):
    @classmethod
    def get_files(cls, dir, date):
        L = []
        for dirpath, dirnames, filenames in os.walk(dir):
            for file in filenames:
                if os.path.splitext(file)[1] == '.xlsx':
                    if file.__contains__(date):
                        file_path = dir + '/' + file
                        size = os.path.getsize(file_path)
                        mtime = time.ctime(os.path.getmtime(file_path))
                        data = {
                            'name': file,
                            'size': size,
                            'time': mtime,
                            'url': settings.EXCEL_URL + file
                        }
                        L.append(data)
        return L

    @classmethod
    def get(cls, request):
        date = request.query_params.get('date')
        data = cls.get_files(settings.EXCEL_DIR, date)
        return Response({
            'status': True,
            'results': data
        })
