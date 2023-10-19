"""
@filename ExampleController.py
@author Parzival
@encoding utf-8
@date 2023-10-19
@lastModify 2023-10-19
@description 测试控制器
"""
import app.WebServer as WebServer
import app.config as config


@WebServer.app.get('/example')
def example():
    return {'服务器地址': config.WEBSERVER_HOST, '服务器端口': config.WEBSERVER_PORT}
