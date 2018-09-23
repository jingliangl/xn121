# coding=utf-8
from rest_framework.pagination import PageNumberPagination
from tools.helper import Dict2obj


class KSPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'size'
    max_page_size = 1000


class RestHelper(object):
    @classmethod
    def get_options(self, viewset, use_filter=True, queryset=None):
        # 搜索待选项
        search_options = {}
        params = viewset.request.query_params
        queryset = queryset if queryset else viewset.get_queryset()
        for name, cl in viewset.filter_class.base_filters.items():
            queryset_ = queryset
            if use_filter:
                if params.get(name):
                    query = params.copy()
                    query.pop(name)
                    for backend in list(viewset.filter_backends):
                        queryset_ = backend().filter_queryset(Dict2obj({'query_params': query}), queryset, viewset)
                else:
                    queryset_ = viewset.filter_queryset(queryset)

            search_options.update({name: queryset_.get_options(cl.name)})

        return search_options

    @classmethod
    def get_search_options(cls, request, qs, filter_class, use_filter=True):
        search_options = {}
        params = request.query_params
        queryset = qs
        for name, cl in filter_class.base_filters.items():
            if use_filter:
                if params.get(name):
                    query = params.copy()
                    query.pop(name)
                    queryset = filter_class(query, queryset=qs, request=request).qs
                else:
                    queryset = filter_class(request.query_params, queryset=qs, request=request).qs

            search_options.update({name: queryset.get_options(cl.name)})

        return search_options
