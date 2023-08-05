# -*- coding:utf-8 -*-
import os
import logging.config

import yaml
from tpspy.client import Client

from restsql.config.load import *

_env_map = {
    '0': False,
    '1': True,
}

CONF_LOGGING_PATH = os.getenv('LOGGING_CONF_PATH', 'conf/logging.yaml')
CONF_DATASOURCE_PATH = os.getenv('CONF_DATASOURCE_PATH', 'conf/datasource.yaml')
CONF_RESTSQL_PATH = os.getenv('CONF_RESTSQL_PATH', 'conf/restsql.yaml')
ENABLE_TPS_FILTER = _env_map[os.getenv('ENABLE_TPS_FILTER', '0')]
TPS_SYS_ID = os.getenv('TPS_SYS_ID', None)
TPS_SYS_SECRET = os.getenv('TPS_SYS_SECRET', None)

tps_client = Client(TPS_SYS_ID, TPS_SYS_SECRET)


# 载入logging配置
def load_logging_conf():
    with open(CONF_LOGGING_PATH, 'r') as f:
        config = yaml.safe_load(f.read())
    if not isinstance(config, dict):
        raise Exception('载入logging配置错误')
    logging.config.dictConfig(config)


def load_config(path):
    """
    载入配置文件。本模块唯一对外暴露函数。
    :param path: 配置文件目录
    :return: None
    """
    with open(path, "r") as fp:  # 配置文件由configmap挂载到镜像路径后传入
        config = yaml.safe_load(fp)
    # 载入数据源
    databases = config.get('databases', [])
    for database in databases:
        name = database.get('name')
        db_type = database.get('db_type')
        host = database.get('host', '127.0.0.1')
        port = database.get('port', 1024)
        user = database.get('user', '')
        password = database.get('password', '')
        db_name = database.get('db_name', '')
        register_database(name=name, db_type=db_type, host=host, port=port, user=user, password=password,
                          db_name=db_name)
    # 载入数据表
    tables = config.get('tables', [])
    for table in tables:
        name = table.get('name')
        table_name = table.get('table_name')
        belong_to = table.get('belong_to')
        fields = table.get('fields')
        register_table(name=name, table_name=table_name, fields=fields, belong_to=belong_to)
