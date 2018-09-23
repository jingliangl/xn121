# coding=utf-8
import datetime
import requests
import random
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.timezone import utc
from django.db import connection
from django.conf import settings


class Helper(object):
    @classmethod
    def get_safe_now(cls):
        if settings.USE_TZ:
            return datetime.datetime.utcnow().replace(tzinfo=utc)

        return datetime.datetime.now()


def random_addr(ext, key):
    i = random.randint(0, 149)
    if ext == 'image':
        addr = 'http://img' + str(i) + '.' + settings.IMAGE_ADDR + key
    else:
        addr = 'http://img' + str(i) + '.' + settings.VIDEO_ADDR + key
    return addr


class Dict2obj(object):
    def __init__(self, dict_data):
        self.__dict__ = dict_data

    def __str__(self):
        return str(self.__dict__)

    def __getattr__(self, item):
        return self.__dict__.get(item)


def decimal_round(value, num=2):
    save_num = '{:.' + str(num) + 'f}'
    return save_num.format(Decimal(str(value)))


def paginator(data, paginate_num=10, page_num=1):
    """
    分页
    """
    paginator = Paginator(data, paginate_num)
    try:
        contacts = paginator.page(page_num)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return contacts


class ESrequests(object):
    @classmethod
    def search(cls, addr=None, headers=None, params=None, must=None, must_not=None, sort=None):
        # must [{'a': '1', 'b': '2'}, {'a': '2', 'b': '3', 'range': {"fans_count": {"gte": 380, "lte": 400}}}]
        # sort 'score'
        if not addr:
            return None
        url = settings.ES_ADDRS.get(addr) + '_search'

        data = {'query': {'bool': {}}}
        if sort:
            data['sort'] = {sort: {'order': 'desc'}}
        if must:
            data['query']['bool']['must'] = must
        if must_not:
            data['query']['bool']['must_not'] = must_not

        r = requests.post(url=url, headers=headers, params=params, json=data).json()
        return r

    @classmethod
    def update(cls, addr=None, headers=None, params=None, ids=None, must_not=None, fields=None, script_params=None, inline=None):
        # ids ['1', '2', '3', ...] , fields {'status': 1, 'name': '2', ...}
        if not addr:
            return None

        if not inline:
            inline = ''
            for k, v in fields.items():
                field = 'ctx._source.' + k + '=' + v + ';'
                inline = inline + field
        data = {
            'query': {
                'bool': {'filter': {'terms': {'_id': ids}}}
            },
            'script': {
                'inline': inline,
                'lang': 'painless'
            }
        }
        if script_params:
            data['script']['params'] = script_params
        if must_not:
            data['query']['bool']['must_not'] = must_not

        params = params if params else {}
        params['refresh'] = 'wait_for'

        url = settings.ES_ADDRS.get(addr) + '_update_by_query'
        r = requests.post(url=url, headers=headers, params=params, json=data).json()
        return r


class DBconnection(object):
    def __init__(self, table):
        self.table = table

    def count(self, where=None):
        count_raw = 'select count(*) from ' + self.table
        count_raw = count_raw + ' where (' + where + ')' if where else count_raw

        with connection.cursor() as cursor:
            cursor.execute(count_raw)
            row = cursor.fetchone()
            count = row[0]
            return count

    def filter(self, where=None, values='*', limit=15, offset=0, order=None):
        raw = 'select ' + values + ' from ' + self.table
        raw = raw + ' where (' + where + ')' if where else raw
        raw = raw + ' order by ' + order if order else raw
        raw = raw + ' limit ' + str(limit)
        raw = raw + ' offset ' + str(offset)

        with connection.cursor() as cursor:
            cursor.execute(raw)
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
