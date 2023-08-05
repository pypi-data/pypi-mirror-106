#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://127.0.0.7:8080'])
# es = Elasticsearch(['http://qapm:Sngapm!=123@9.134.92.202:9200'])

"""
PUT /exclude_test
{
    "mappings": {
        "record": {
            "properties": {
                "id": {
                    "type": "keyword"
                },
                "cpu1": {
                    "type": "integer"
                },
                "cpu2": {
                    "type": "integer"
                },
                "cpu3": {
                    "type": "integer"
                },
                "cpu4": {
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
    es.index(index='exclude_test', doc_type='record', id=i, body={
        "id": i,
        "cpu1": random.randint(0, 100),
        "cpu2": random.randint(0, 100),
        "cpu3": random.randint(0, 100),
        "cpu4": random.randint(0, 100),
        "event_time": (now + datetime.timedelta(
            seconds=i + random.randint(1, 100))).strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"),
    })
