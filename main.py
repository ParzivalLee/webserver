"""
@filename WebServer.py
@author Parzival
@date 2023-07-24
@lastModified 2023-07-24
@encoding utf-8
@description 网页服务器入口
控制器从此处导入
"""
import config
import uvicorn
import WebServer

"""执行程序"""
uvicorn.run(WebServer.app, host=config.WEBSERVER_HOST, port=config.WEBSERVER_PORT)
