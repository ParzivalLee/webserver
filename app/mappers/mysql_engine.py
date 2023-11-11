"""
@filename mysql_engine.py
@author Parzival
@encoding utf-8
@date 2023-11-11
@description MySQL引擎
"""
import app.config as config
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

# MySQL连接引擎
engine: Engine = create_engine("mysql+pymysql://%s:%s@%s:%d/%s" % (
    config.MYSQL_USERNAME,
    config.MYSQL_PASSWORD,
    config.MYSQL_HOST,
    config.MYSQL_PORT,
    config.MYSQL_DATABASE
))
