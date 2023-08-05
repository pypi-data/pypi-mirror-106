#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import string

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://127.0.0.7:8080'])
# es = Elasticsearch(['http://qapm:Sngapm!=123@9.134.92.202:9200'])

"""
PUT /str_test
{
    "mappings": {
        "record": {
            "properties": {
                "id": {
                    "type": "keyword"
                },
                "str": {
                    "type": "text",
                    "index": false
                }
            }
        }
    }
}
"""

for i in range(0, 86400):
    es.index(index='str_test', doc_type='record', id=i, body={
        "id": i,
        "str": (i, ''.join(random.sample(string.ascii_letters + string.digits, 8))),
    })
