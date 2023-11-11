"""
@filename mysql_engine.py
@author Parzival
@encoding utf-8
@date 2023-11-11
@description MySQL引擎
"""
from sqlalchemy import text, TextClause
from .mysql_engine import engine


# 向数据表写入一条新的记录
def insert(data: dict, table_name: str) -> int:
    """
    向数据表写入一条新的记录
    :param data: 数据
    :param table_name: 数据表
    :return: 是否写入成功
    """
    fields: tuple = tuple(data.keys())
    fields_str: str = ','.join(fields)  # 构造字段字符串
    values_str: str = ','.join([':%s' % i for i in fields])  # 构造值字符串
    sql: TextClause = text('INSERT INTO %s(%s) VALUES(%s)' % (table_name, fields_str, values_str))  # 构造SQL语句
    with engine.connect() as connection:
        try:
            connection.execute(sql, data)
            connection.commit()
            connection.close()
            return 0
        except Exception as e:
            connection.rollback()
            connection.close()
            print(e)
            return -1


# 从数据表删除记录
def delete(query: dict, table_name: str) -> int:
    """
    从数据表删除记录
    :param query: 检索字段
    :param table_name: 数据表
    :return: 是否删除成功
    """
    fields: tuple = tuple(query.keys())
    query_str: str = ' AND '.join(['%s=:%s' % (i, i) for i in fields])  # 构造检索字符串
    sql: TextClause = text('DELETE FROM %s WHERE %s' % (table_name, query_str))  # 构造SQL语句
    with engine.connect() as connection:
        try:
            connection.execute(sql, query)
            connection.commit()
            connection.close()
            return 0
        except Exception as e:
            connection.rollback()
            connection.close()
            print(e)
            return -1


# 修改数据表中的记录
def update(query: dict, data: dict, table_name: str) -> int:
    """
    修改数据表中的记录
    :param query: 要修改的数据
    :param data: 要修改为的值
    :param table_name: 要修改的数据表
    :return: 是否修改成功
    """
    query_fields: tuple = tuple(query.keys())  # 要检索的字段
    query_fields_str: str = ' AND '.join(['%s=:_%s' % (i, i) for i in query_fields])  # 构造检索字符串(添加一个下划线用于区别)

    data_fields: tuple = tuple(data.keys())  # 要修改的字符
    data_fields_str: str = ','.join(['%s=:%s' % (i, i) for i in data_fields])  # 构造修改字符串

    # 批量修改键
    for i in query:
        query['_' + i] = query[i]
        del query[i]

    sql: TextClause = text('UPDATE %s SET %s WHERE %s' % (table_name, data_fields_str, query_fields_str))  # 构造SQL语句

    data.update(query)  # 合并字典
    with engine.connect() as connection:
        try:
            connection.execute(sql, data)
            connection.commit()
            connection.close()
            return 0
        except Exception as e:
            connection.rollback()
            connection.close()
            print(e)
            return -1


# 检索数据表中的记录
def select(query: dict, fields: tuple, table_name: str) -> list:
    """
    检索数据表中的记录
    :param query: 检索内容
    :param fields: 要查询的字段
    :param table_name: 数据表
    :return: 数据表记录值
    """
    query_fields: tuple = tuple(query.keys())  # 要检索的字段
    query_fields_str: str = ' AND '.join(['%s=:_%s' % (i, i) for i in query_fields])  # 构造检索字符串(添加一个下划线用于区别)

    select_fields_str: str = ','.join(fields)

    sql: TextClause = text('SELECT %s FROM %s WHERE %s' % (select_fields_str, table_name, query_fields_str))  # 构造SQL语句

    with engine.connect() as connection:
        try:
            pre_result: list = list(connection.execute(sql, query).fetchall())
        except Exception as e:
            print(e)
            return []

    result: list = []  # 构造结果列表
    for i in pre_result:
        result.append(dict(zip(fields, i)))

    return result
