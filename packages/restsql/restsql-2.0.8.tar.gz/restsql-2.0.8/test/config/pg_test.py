import unittest

from restsql import RestSQL
from restsql.config.load import *


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        register_database(
            name='pg_test',
            db_type='POSTGRESQL',
            host='127.0.0.1',
            port=5432,
            user='oliverdd',
            password='dzp',
            db_name='test',
        )
        register_table(
            name='str_test',
            table_name='public.str_test',
            fields={
                'id': 'int',
                'str': 'string',
            },
            belong_to='pg_test',
        )
        register_table(
            name='bool_test',
            table_name='public.bool_test',
            fields={
                'id': 'int',
                'isdog': 'bool',
            },
            belong_to='pg_test',
        )
        register_table(
            name='mem_time_table',
            table_name='public.mem_time_table',
            fields={
                'id': 'int',
                'mem_used': 'int',
                'event_time': 'datetime',
            },
            belong_to='pg_test'
        )
        register_table(
            name='exclude_test',
            table_name='public.exclude_test',
            fields={
                'id': 'int',
                'cpu1': 'int',
                'cpu2': 'int',
                'cpu3': 'int',
                'cpu4': 'int',
                'event_time': 'datetime',
            },
            belong_to='pg_test'
        )

    def tearDown(self):
        print("----------TEST END---------->")

    def setUp(self):
        print("<----------TEST BEGIN----------")


    def test_single_main1(self):
        query = {
            'select': {
                'from': 'pg_test.mem_time_table',
                'fields': ['id', 'mem_used', 'event_time'],
                'filter': {
                    'event_time__gte': '2020-11-25T00:00:00.000Z',
                    'event_time__lte': '2020-11-25T23:59:59.000Z',
                },
                'aggregation': [],
                'group_by': [],
                'limit': 1000,
            },
            'join': [
            ],
            'sort': ['id'],
            'fields': ['id@id', 'mem_used@memory', 'event_time@time'],
            'limit': 1000,
        }
        df = RestSQL.query(query_dict=query)
        print(df)


    def test_single_main2(self):
        query = {
            'select': {
                'from': 'pg_test.exclude_test',
                'fields': ['id'],
                'filter': {
                    'event_time__gte': '2020-11-25T00:00:00.000Z',
                    'event_time__lte': '2020-11-25T23:59:59.000Z',
                },
                'aggregation': ['cpu2__avg', 'cpu3__avg', 'cpu1__avg', 'cpu4__avg'],
                'group_by': ['id'],
            },
            'join': [
            ],
            'sort': ['id'],
            'fields': ['id@id', 'cpu2__avg@cpu2', 'cpu3__avg@cpu3', 'cpu4__avg@cpu4', 'cpu1__avg@cpu1'],
            'limit': 1000,
        }
        df = RestSQL.query(query_dict=query)
        print(df)


    def test_single_main3(self):
        query = {
            'select': {
                'from': 'pg_test.exclude_test',
                'fields': ['id'],
                'filter': {
                    'event_time__gte': '2020-11-25T00:00:00.000Z',
                    'event_time__lte': '2020-11-25T23:59:59.000Z',
                },
                'aggregation': ['cpu2__avg', 'cpu3__avg', 'cpu1__avg', 'cpu4__avg'],
                'group_by': ['id'],
            },
            'join': [
            ],
            'sort': ['id'],
            'fields': ['id@id', 'cpu2__avg@exclude', 'cpu3__avg@exclude', 'cpu4__avg@exclude', 'cpu1__avg@exclude',
                       '(cpu1__avg+cpu2__avg+cpu3__avg+cpu4__avg)/4@cpu'],
            'limit': 1000,
        }
        df = RestSQL.query(query_dict=query)
        print(df)


    def test_single_main4(self):
        query = {
            'select': {
                'from': 'pg_test.mem_time_table',
                'fields': ['id'],
                'filter': {
                    # 'event_time__gte': '2020-11-25T00:00:00.000Z',
                    # 'event_time__lte': '2020-11-25T23:59:59.000Z'
                },
                'aggregation': ['event_time__min'],
                'group_by': ['id'],
                'limit': 1000,
            },
            'join': [
            ],
            'sort': ['id'],
            'fields': ['id@id', 'event_time__min@event_time'],
            'limit': 1000,
        }
        df = RestSQL.query(query_dict=query)
        print(df)
        print(df.shape[0])

    def test_single_main5(self):
        query = {
            'select': {
                'from': 'pg_test.bool_test',
                'fields': ['id', 'isdog'],
                'filter': {
                    'id__gte': 10,
                    'id__lte': 20
                },
                'aggregation': [],
                'group_by': [],
                'limit': 1000,
            },
            'join': [
            ],
            'sort': ['id'],
            'fields': ['id@id', 'isdog@isdog'],
            'limit': 1000,
        }
        df = RestSQL.query(query_dict=query)
        print(df)
        print(df.shape[0])


    def test_single_join(self):
        query = {
            'select': {
                'from': 'pg_test.mem_time_table',
                'fields': ['id', 'mem_used', 'event_time'],
                'filter': {
                    'event_time__gte': '2020-11-25T00:00:00.000Z',
                    'event_time__lte': '2020-11-25T23:59:59.000Z',
                },
                'aggregation': [],
                'group_by': [],
                'limit': 1000,
            },
            'join': [
                {
                    'on': {'id': 'id'},
                    'type': "left_join",
                    'query': {
                        'select': {
                            'from': 'pg_test.exclude_test',
                            'fields': ['id'],
                            'filter': {
                                'event_time__gte': '2020-11-25T00:00:00.000Z',
                                'event_time__lte': '2020-11-25T23:59:59.000Z',
                            },
                            'aggregation': ['cpu2__avg', 'cpu3__avg', 'cpu1__avg', 'cpu4__avg'],
                            'group_by': ['id'],
                        },
                    },
                    'export': ['cpu2__avg@cpu2', 'cpu3__avg@cpu3', 'cpu1__avg@cpu1', 'cpu4__avg@cpu4'],
                },
            ],
            'sort': ['id'],
            'fields': ['id@id', 'mem_used@memory', 'event_time@time', 'cpu2@cpu2', 'cpu3@cpu3', 'cpu4@cpu4',
                       'cpu1@cpu1'],
            'limit': 1000,
        }
        df = RestSQL.query(query_dict=query)
        print(df)


if __name__ == '__main__':
    unittest.main()
