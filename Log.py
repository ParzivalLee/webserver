"""
@filename WebServer.py
@author Parzival
@date 2023-8-10
@lastModified 2023-8-10
@encoding utf-8
@description 网页服务器日志类
"""

import time


def printLog(msg_type: str, msg: str) -> None:
    """
    输出日志内容
    :param msg_type: 信息类型
    :param msg: 信息内容
    :return: None
    """
    print('[%s] %s: %s' % (msg_type, time.strftime('%Y-%m-%d %H:%M:%S'), msg))


def printNotice(msg: str) -> None:
    """
    打印通知信息
    :param msg: 信息内容
    :return: None
    """
    # 输出信息标识符为绿色
    print('\033[0;32m[Notice]\033[0m %s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))


def printWarning(msg: str) -> None:
    """
    打印警告信息
    :param msg: 信息内容
    :return: None
    """
    # 输出信息标识符为黄色
    print('\033[0;33m[Warning]\033[0m %s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))


def printError(msg: str) -> None:
    """
    打印错误信息
    :param msg: 信息内容
    :return: None
    """
    # 输出信息标识符为红色
    print('\033[0;31m[Error]\033[0m %s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))
