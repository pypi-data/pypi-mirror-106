#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random
import string

import psycopg2

TABLE_NAME = "bool_test"


def create_table(cur):
    cur.execute("\
    CREATE TABLE IF NOT EXISTS {} (\
        id int primary key,\
        isdog boolean\
    )\
    ".format(TABLE_NAME))


conn = psycopg2.connect(database="test", user="oliverdd", password="dzp", host="127.0.0.1", port="5432")

cur = conn.cursor()

create_table(cur=cur)

for i in range(0, 86400):
    cur.execute("INSERT INTO {} (id, isdog) \
      VALUES ( %s, %s)".format(TABLE_NAME), (i, random.randint(0, 1) == 0))
conn.commit()
conn.close()

if __name__ == '__main__':
    pass