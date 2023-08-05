#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random

import psycopg2

TABLE_NAME = "mem_time_table"


def create_table(cur):
    cur.execute("\
    CREATE TABLE IF NOT EXISTS {} (\
        id int primary key,\
        mem_used int,\
        event_time timestamp with time zone\
    )\
    ".format(TABLE_NAME))


conn = psycopg2.connect(database="test", user="oliverdd", password="dzp", host="127.0.0.1", port="5432")

cur = conn.cursor()

create_table(cur=cur)

now = datetime.datetime.strptime("2020-11-25 00:00:00", "%Y-%m-%d %H:%M:%S")

for i in range(0, 86400):
    cur.execute("INSERT INTO {} (id,mem_used, event_time) \
              VALUES (%s, %s,%s)".format(TABLE_NAME), (i, random.randint(0, 100),
                                                       (now + datetime.timedelta(
                                                           seconds=i + random.randint(1, 100))).strftime(
                                                           "%Y-%m-%d %H:%M:%S")))
conn.commit()
conn.close()
