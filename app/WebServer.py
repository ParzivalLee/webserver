"""
@filename WebServer.py
@author Parzival
@date 2023-07-24
@lastModified 2023-07-24
@encoding utf-8
@description 网页服务器
"""
import pymongo
from . import config
from fastapi import FastAPI

"""全局变量"""
global_variable: dict = dict()

"""FastAPI服务"""
app = FastAPI(debug=True)

