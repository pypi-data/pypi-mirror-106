#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://127.0.0.7:8080'])
# es = Elasticsearch(['http://qapm:Sngapm!=123@9.134.92.202:9200'])

"""
PUT /mem_time_table
{
    "mappings": {
        "record": {
            "properties": {
                "id": {
                    "type": "keyword"
                },
                "mem_used": {
                    "type": "integer"
                },
                "event_time": {
                    "type": "date"
                }
            }
        }
    }
}
"""

now = datetime.datetime.strptime("2020-11-25 00:00:00", "%Y-%m-%d %H:%M:%S")

for i in range(0, 86400):
    es.index(index='mem_time_table', doc_type='record', id=i, body={
        "id": i,
        "mem_used": random.randint(0, 100),
        "event_time": (now + datetime.timedelta(
            seconds=i + random.randint(1, 100))).strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"),
    })

