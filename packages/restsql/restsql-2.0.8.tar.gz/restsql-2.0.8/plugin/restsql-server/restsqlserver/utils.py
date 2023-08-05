# -*- coding:utf-8 -*-
import datetime
import json

import pandas as pd
from restsql.exception import *


def grafana_table_format(dataframe):
    """
    将查询结果格式化为table格式:
    {
        'type': 'table',
        'columns': [
            {
                'text': '字段名称',
                'type': 'string'/'number'/'time'
            },
            ...
        ],
        'rows': [
            [...],
            [...],
            ...
        ]
    }
    :param dataframe: 查询到的dataframe
    :return:
    """
    if isinstance(dataframe, pd.DataFrame):
        columns = []
        for (column, series) in zip(list(dataframe), dataframe.dtypes):
            kind = series.kind
            if kind == 'i' or kind == 'u' or kind == 'f' or kind == 'c':
                text = 'number'
            elif kind == 'M':
                text = 'time'
            elif kind == 'm':
                raise ProgramConfigException(303, '不应该出现timedelta格式。联系开发者以解决此问题。')
            else:
                text = 'string'
            columns.append({
                'text': column,
                'type': text,
            })
        data_dict = json.loads(dataframe.to_json(orient='split'))
        return {
            'columns': columns,
            'rows': data_dict.get('data'),
            'type': 'table'
        }
    else:
        raise RunningException(1, 'table format失败: 需要dataframe实例而不是{}', type(dataframe))


def grafana_timeserie_format(dataframe, time_shift, time_shift_dimension, time_agg, time_agg_dimension, begin_time,
                             end_time):
    """
    将查询结果格式化为timeserie格式:
    {
        "target": "字段名",
        "datapoints": [
            [..],  // 只会有两个字段，第一个是数值、第二个是时间字段(用13位timestamp)
            ...
        ]
    }
    :param dataframe: 待格式化的dataframe
    :param time_shift: 需要shift的时间基量
    :param time_shift_dimension: 需要shift的时间维度
    :param time_agg: 需要聚合的时间基量
    :param time_agg_dimension: 需要聚合的时间维度
    :param begin_time: 聚合开始时间
    :param end_time: 聚合结束时间
    :return:
    """
    if isinstance(dataframe, pd.DataFrame):
        if dataframe.shape[0] == 0 or dataframe.shape[1] == 0:  # 数据为空时返回空df
            return {
                'target': '',
                'datapoints': [],
            }
        if dataframe.shape[1] != 2:
            raise RunningException(1, 'timeserie format需要两个字段，并且其中一个是时间戳格式。当前共有{}个字段。', dataframe.shape[1])
        first_col_type = dataframe.dtypes[0].kind
        second_col_type = dataframe.dtypes[1].kind
        if first_col_type == 'm':
            raise ProgramConfigException(303, '不应该出现timedelta格式。联系开发者以解决此问题。')
        if first_col_type == 'M':  # 第一列是时间字段，则换到第二列
            cols = list(dataframe.columns)
            cols = [cols[-1]] + cols[:-1]
            dataframe = dataframe[cols]
            second_col_type = first_col_type
        if second_col_type == 'm':
            raise ProgramConfigException(303, '不应该出现timedelta格式。联系开发者以解决此问题。')
        elif second_col_type != 'M':
            raise RunningException(1, 'timeserie format需要两个字段，并且其中一个是时间字段。')
        # 将datetime转为timedelta
        second_col = list(dataframe)[1]
        # dataframe[second_col] = dataframe[second_col].astype(int)/10**6
        # dataframe[second_col] = dataframe[second_col].astype(int)
        dataframe[second_col] = pd.to_datetime(dataframe[second_col]).dt.tz_localize(None)
        dataframe[second_col] = pd.to_timedelta(dataframe[second_col]).dt.total_seconds().astype('int64')  # 为啥会自动+8？？？
        dataframe[second_col] = dataframe[second_col].apply(lambda x: (x-28800) * 1000)
        dataframe.sort_values(by=list(dataframe)[1], ascending=True, inplace=True)  # 时间排序：从小到大
        time_var = _cal_shift_time(time_shift, time_shift_dimension)
        if time_var != 0:  # Time shift
            dataframe[1] = dataframe[1].map(lambda x: x + datetime.timedelta(seconds=time_var))
        time_var = _cal_shift_time(time_agg, time_agg_dimension)
        if time_var != 0:  # Time agg
            pass  # TODO: agg
        data_dict = json.loads(dataframe.to_json(orient='split'))
        return {
            'target': data_dict.get('columns')[0],
            'datapoints': data_dict.get('data'),
        }
    else:
        raise RunningException(1, 'timeserie format失败: 需要dataframe实例而不是{}', type(dataframe))


def _cal_shift_time(time_var, dimension):
    """
    同比环比是通过前端预先移动时间范围实现的，因此需要在后端将时间的范围移动回框内。
    也就是将时间往反反向移动，以实现同框展示环比同比。
    :param time_var: 时间变量
    :param dimension: 时间单位
    :return: 计算后的秒数
    """
    if dimension == 's':
        time_var = int(int(time_var) * 1)
    elif dimension == 'mi':
        time_var = int(int(time_var) * 60 * 1)
    elif dimension == 'h':
        time_var = int(int(time_var) * 60 * 60 * 1)
    elif dimension == 'd':
        time_var = int(int(time_var) * 24 * 60 * 60 * 1)
    elif dimension == 'w':
        time_var = int(int(time_var) * 7 * 24 * 60 * 60 * 1)
    elif dimension == 'mo':
        time_var = int(int(time_var) * 30 * 7 * 24 * 60 * 60 * 1)
    elif dimension == 'y':
        time_var = int(int(time_var) * 365 * 24 * 60 * 60 * 1)
    else:
        raise RunningException(1, "格式化为grafana.timeserie格式出错: 未知的dimension类型 {}", dimension)
    return time_var
