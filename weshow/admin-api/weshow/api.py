# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class WeshowView(APIView):
    @classmethod
    def get_data(cls):
        tv = settings.TV
        data = {}
        for k, v in tv:
            with open(v, 'r') as f:
                value = json.load(f)
                data[k] = value
        return data

    @classmethod
    def get(cls, request):
        id = request.query_params.get('id')
        tv = request.query_params.get('tv')
        data = cls.get_data()
        ret = data.get(tv, [])
        if id is not None:
            for item in ret:
                if item.get('id') == id:
                    ret = item
		    name = ret.get('name')
		    if name and len(name) > 10:
		        ret['name'] = name[:-10]
		        ret['time'] = name[-10:]
                    break

        return Response({
            'status': True,
            'results': ret
        })
