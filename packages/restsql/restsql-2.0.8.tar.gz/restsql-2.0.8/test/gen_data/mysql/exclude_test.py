#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import random

import MySQLdb

TABLE_NAME = "exclude_test"


def create_table(cur):
    cur.execute("\
    CREATE TABLE IF NOT EXISTS {} (\
        id int primary key,\
        cpu1 int,\
        cpu2 int,\
        cpu3 int,\
        cpu4 int,\
        event_time timestamp\
    )\
    ".format(TABLE_NAME))


conn = MySQLdb.connect(db="test", user="root", passwd="dzp", host="127.0.0.1", port=3306)

cur = conn.cursor()

create_table(cur=cur)

now = datetime.datetime.strptime("2020-11-25 00:00:00", "%Y-%m-%d %H:%M:%S")

for i in range(0, 86400):
    cur.execute("INSERT INTO exclude_test (id,cpu1,cpu2, cpu3, cpu4, event_time) \
      VALUES ({},{},{},{},{},'{}')".format(i, random.randint(0, 100), random.randint(0, 100),
                                           random.randint(0, 100), random.randint(0, 100),
                                           (now + datetime.timedelta(seconds=i + random.randint(1, 100))).strftime(
                                               "%Y-%m-%d %H:%M:%S")))
conn.commit()
conn.close()

if __name__ == '__main__':
    pass
