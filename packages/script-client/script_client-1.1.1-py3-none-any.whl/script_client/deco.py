
from loguru import logger
from script_client.func_map import fm



def register(app='',path='',timeout=0):
    '''
    注册为回调函数
    :param app: app_code
    :param path: path
    :param timeout: timeout 本期没做无效
    :return:
    '''
    def deco(func):
        fm.add_map(app=app,path=path,func=func,timeout=timeout)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return deco