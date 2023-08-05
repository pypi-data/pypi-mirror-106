#!/usr/bin/env python
# -*- coding:utf-8 -*-
from restsql import EsEngine

query = {
    "select": {
        "from": "es_test.mem_time_table",
        "fields": ["time_stamp"],
        "filter": {
            "time_stamp__gte": "2021-01-29 13:49:24",
            "time_stamp__lte": "2021-01-29 19:49:24"
        },
        "aggregation": ["total_cnt__avg"],
        "group_by": ["time_stamp"],
        "limit": 1000
    },
    "join": [
    ],
    "sort": ["time_stamp"],
    "fields": ["time_stamp@time_stamp", "total_cnt__avg@total_cnt"],
    "limit": 1000
}

if __name__ == '__main__':
    engine = EsEngine()
    print(engine.parse(query["select"]))


