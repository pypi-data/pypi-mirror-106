#!/usr/bin/env python
# -*- coding:utf-8 -*-

from restsql import register_database, register_table
from restsql.entry import RestSQL

register_database(
            name='es_test',
            db_type='ELASTICSEARCH',
            host='oliverdd.cn:8080',
        )
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
            table_name='str_test',
            fields={
                'id': 'int',
                'str': 'string',
            },
            belong_to='pg_test',
        )
register_table(
            name='mem_time_table',
            table_name='mem_time_table',
            fields={
                'id': 'int',
                'mem_used': 'int',
                'event_time': 'datetime',
            },
            belong_to='pg_test'
        )
register_table(
            name='exclude_test',
            table_name='exclude_test',
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
register_table(
            name='str_test',
            table_name='str_test',
            fields={
                'id': 'int',
                'str': 'string',
            },
            belong_to='es_test',
        )
register_table(
            name='mem_time_table',
            table_name='mem_time_table',
            fields={
                'id': 'int',
                'mem_used': 'int',
                'event_time': 'datetime',
            },
            belong_to='es_test'
        )
register_table(
            name='exclude_test',
            table_name='exclude_test',
            fields={
                'id': 'int',
                'cpu1': 'int',
                'cpu2': 'int',
                'cpu3': 'int',
                'cpu4': 'int',
                'event_time': 'datetime',
            },
            belong_to='es_test'
        )

query = {
    "select": {
        "from": "es_test.mem_time_table",
        "fields": ["id", "mem_used", "event_time"],
        "filter": {
            "event_time__gte": "2020-11-25T00:00:00.000Z",
            "event_time__lte": "2020-11-25T23:59:59.000Z"
        },
        "aggregation": [],
        "group_by": [],
        "limit": 10000
    },
    "join": [
        {
            "on": {"id": "id"},
            "type": "left_join",
            "query": {
                "select": {
                    "from": "es_test.exclude_test",
                    "fields": ["id"],
                    "filter": {
                        "event_time__gte": "2020-11-25T00:00:00.000Z",
                        "event_time__lte": "2020-11-25T23:59:59.000Z"
                    },
                    "aggregation": ["cpu2__avg", "cpu3__avg", "cpu1__avg", "cpu4__avg"],
                    "group_by": ["id"]
                }
            },
            "export": ["cpu2__avg@cpu2", "cpu3__avg@cpu3", "cpu1__avg@cpu1", "cpu4__avg@cpu4"]
        }
    ],
    "sort": ["id"],
    "fields": ["id@id", "mem_used@memory", "event_time@time"],
    "limit": 10000
}

if __name__ == '__main__':
    result = RestSQL.query(query_dict=query)
    print(result)
