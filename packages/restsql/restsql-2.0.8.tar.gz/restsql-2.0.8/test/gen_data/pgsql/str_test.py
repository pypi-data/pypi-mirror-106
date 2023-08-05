#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random
import string

import psycopg2

TABLE_NAME = "str_test"


def create_table(cur):
    cur.execute("\
    CREATE TABLE IF NOT EXISTS {} (\
        id int primary key,\
        str varchar(50)\
    )\
    ".format(TABLE_NAME))


conn = psycopg2.connect(database="test", user="oliverdd", password="dzp", host="127.0.0.1", port="5432")

cur = conn.cursor()

create_table(cur=cur)

now = datetime.datetime.strptime("2020-11-25 00:00:00", "%Y-%m-%d %H:%M:%S")

for i in range(0, 86400):
    cur.execute("INSERT INTO {} (id, str) \
      VALUES ( %s, %s)".format(TABLE_NAME, ), (i, ''.join(random.sample(string.ascii_letters + string.digits, 8))))
conn.commit()
conn.close()
