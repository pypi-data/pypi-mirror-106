#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import getopt
import json
import logging
import sys

from config import load_config, ENABLE_TPS_FILTER, CONF_RESTSQL_PATH, tps_client, TPS_SYS_ID
from utils import grafana_table_format, grafana_timeserie_format

import web
import restsql as rql

logger = logging.getLogger(__name__)

urls = (
    "/restsql", "ConnectionView",
    "/restsql/", "ConnectionView",
    "/restsql/query", "QueryView",
    "/restsql/search", "VariableView",
    "/restsql/find_options", "FieldView",
    "/restsql/find_tables", "TableView"
)


class QueryView(object):
    """
    查询query接口
    request data:
    {
        'format': '...',
        (for grafana.timeserie
        'beginTime': ,
        'endTime':
        )
        'data':
        [
            {
                'query':
                {
                    ...
                },
                (for grafana.timeserie
                'timeShift': ,
                'timeShiftDimension': '',
                'timeAgg': ,
                'timeAggDimension': ''
                )
            },
            {
                ...
            }
        ]
    }
    """
    TABLE = 'grafana.table'
    TIMESERIE = 'grafana.timeserie'
    NORMAL = 'normal'

    def POST(self):
        logger.info("QueryView active.")
        try:
            data = json.loads(web.data())
        except Exception as e:
            logging.exception(e)
            raise web.internalerror('解析json时发生错误')
        grafana_type = data.get('format', 'normal')
        begin_time = data.get('beginTime', None)
        end_time = data.get('endTime', None)
        response_data = []  # 存储多query查询的结果
        for query_data in data.get('data'):
            # 获取相关信息
            query_dict = query_data.get('query')
            time_shift = query_data.get('timeShift', None)
            time_shift_dimension = query_data.get('timeShiftDimension', None)
            time_agg = query_data.get('timeAgg', None)
            time_agg_dimension = query_data.get('timeAggDimension', None)
            # 查询
            try:
                result_df = rql.RestSQL.query(query_dict)
            except rql.RestSqlExceptionBase as e:
                logger.error('query查询失败: %s %s', e.code, e.message)
                raise web.internalerror('query查询失败: \
                                         错误代码: {}; \
                                         错误信息: {}'.format(e.code, e.message))
            except Exception as e:
                logger.error('query查询时发生未知异常: %s', e)
                logging.exception(e)
                raise web.internalerror('查询时发生未知异常: {}'.format(e))
            logger.debug('RestSQL.query\'s raw result is:\n %s', result_df)
            query_result = None
            try:
                if grafana_type == QueryView.NORMAL:
                    query_result = json.loads(result_df.to_json(orient='records'))
                elif grafana_type == QueryView.TABLE:
                    query_result = grafana_table_format(result_df)
                elif grafana_type == QueryView.TIMESERIE:
                    query_result = grafana_timeserie_format(result_df, time_shift, time_shift_dimension, time_agg,
                                                            time_agg_dimension, begin_time, end_time)
                else:
                    raise rql.RunningException(1, 'query查询后格式化遇到未知grafana type: {}', grafana_type)
            except rql.RestSqlExceptionBase as e:
                logger.error(e.message)
                raise web.internalerror('query数据格式化失败: \
                                         错误代码: {}; \
                                         错误信息: {}'.format(e.code, e.message))
            response_data.append(query_result)
        return json.dumps({
            'status': 'ok',
            'data': response_data
        })

    def OPTIONS(self):
        """
        用以声明支持跨域查询
        :return:
        """
        return


class VariableView(object):
    """
    查询variable接口
    request:
    {
        'target': '...' # example: {"select": "id", "from": "user"}
    }
    response:
        ['...', ...]
    """

    def POST(self):
        logger.info("VariableView active.")
        try:
            data = json.loads(web.data())
        except Exception as e:
            logger.error('[VariableView] 解析json时发生错误')
            logging.exception(e)
            raise web.internalerror('[VariableView] 解析json时发生错误，请查看运行日志')
        # 提取变量
        target = data.get('target')
        if target is None:
            raise web.internalerror('[VariableView] 查询格式不正确: 无target字段')
        select_part = target.get('select', None)
        from_part = target.get('from', None)
        if select_part is None:
            raise web.internalerror('[VariableView] 查询格式不正确，需要select字段')
        if from_part is None:
            raise web.internalerror('[VariableView] 查询格式不正确，需要from字段')
        # 查询
        query_dict = self._gen_query(select_part, from_part)
        try:
            result_df = rql.RestSQL.query(query_dict)
        except rql.RestSqlExceptionBase as e:
            logger.error('[VariableView] 查询失败')
            logging.exception(e)
            raise web.internalerror('[VariableView] 查询失败: \
                        错误代码: {}; \
                        错误信息: {}'.format(e.code, e.message))
        except Exception as e:
            logger.error('[VariableView] 查询失败: 未知异常')
            logging.exception(e)
            raise web.internalerror('[VariableView] 查询失败: 未知异常，请查看运行日志')
        result_dict = result_df.to_dict()
        return json.dumps({
            'status': 'ok',
            'data': tuple(result_dict.get(select_part).values())
        })

    def _gen_query(self, select_part, from_part):
        """
        根据variable查询的输入语句，生成restql查询。
        :param select_part: select字段
        :param from_part: from字段
        :return:
        """
        return {
            'select': {
                'from': from_part,
                'fields': [select_part],
                'group_by': [select_part],
                'limit': 10000
            },
            'sort': [select_part],
            'fields': ['{}@{}'.format(select_part, select_part)],
            'limit': 10000
        }


class TableView(object):
    """
    查询可选表的接口
    response:
    {
        'status': 'ok',
        'data': ['...', ...]
    }
    """

    def GET(self):
        logger.info("TableView active.")
        return json.dumps({
            'status': 'ok',
            'data': list(rql.index4table.keys())
        })


class FieldView(object):
    """
    查询表字段接口
    request:
        {
            'tableName': '...'<String>
        }
    response:
        ['...', ...]
    """

    def POST(self):
        logger.info("FieldView active.")
        try:
            data = json.loads(web.data())
        except Exception as e:
            logger.error('[FieldView] 解析json时发生错误')
            logging.exception(e)
            raise web.internalerror('[FieldView] 解析json时发生错误，请查看运行日志')
        table_name = data.get("tableName")
        table = rql.index4table.get(table_name, None)
        if table is None:
            raise web.internalerror('[FieldView] 需查询字段的表{}不存在'.format(table_name))
        return json.dumps({
            'status': 'ok',
            'data': list(table.fields.keys())
        })


class ConnectionView(object):
    """
    用于测试后端运行中
    """

    def GET(self):
        logger.info("ConnectionView active.")
        return 'Connection successful!'


def verify_token():
    token = web.cookies().get('token')
    if not token:
        logger.warning('空token访问')
        raise web.internalerror(
            'token为空. 请使用正规途径访问.'
        )
    is_valid, msg = tps_client.auth.check_token(token)
    if not is_valid:
        logger.warning('无效token: %s. %s', token, msg)
        raise web.internalerror(
            '无效token: {}. {}.'.format(token, msg)
        )
    user_id = web.cookies().get('user_id')
    sys_id = TPS_SYS_ID
    p_id = web.cookies().get('p_id')
    can_access, _ = tps_client.get_user_to_target_access(user_id, '{}::{}'.format(sys_id, p_id), token)
    if not can_access:
        logger.warning('用户%s非法访问资源%s::%s.', user_id, sys_id, p_id)
        raise web.internalerror(
            '当前用户({})无权限访问资源{}.'.format(user_id, p_id)
        )


def enable_acao():
    """
    提供跨域支持
    """
    web.header('Access-Control-Allow-Origin', '*')
    web.header('Access-Control-Allow-Headers',
               'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, '
               'Access-Control-Allow-Methods')
    web.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


app = web.application(urls, globals())

if __name__ == "__main__":
    logger.info('restsql server为您服务!')
    try:
        load_config(CONF_RESTSQL_PATH)
    except Exception as e:
        logger.critical('载入配置失败')
        logging.exception(e)
        sys.exit()
    if ENABLE_TPS_FILTER:
        logger.info('TPS过滤关闭')
        app.add_processor(web.loadhook(verify_token))
    else:
        logger.info('TPS过滤开启')
    app.add_processor(web.unloadhook(enable_acao))

    logger.info('配置载入完成')
    app.run()
