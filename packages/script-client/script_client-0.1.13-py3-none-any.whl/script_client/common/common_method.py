'''
common method
'''

import os
import json
import socket
from loguru import logger
from script_client.common.my_requests import MyRequests
from script_client.const import config
import shutil

def replace_str(s):
    s = s.replace('\r\n','')
    # s = s.replace('\', '')
    return s

def get_local_ip():
    local_ip = ""
    try:
        socket_objs = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
        ip_from_ip_port = [(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in socket_objs][0][1]
        ip_from_host_name = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
        local_ip = [l for l in (ip_from_ip_port, ip_from_host_name) if l][0]
    except (Exception) as e:
        print("get_local_ip found exception : %s" % e)
    return local_ip if("" != local_ip and None != local_ip) else socket.gethostbyname(socket.gethostname())



def is_none(kwargs):
    '''
    0、空、None、False 外都算 True
    :param kwargs:
    :return:
    '''
    ll = []
    for k,v in kwargs.items():
        ll.append(v)
    if all(ll):
        return False
    return True



def del_path(path):
    '''
    删文件夹，以及文件夹内的文件
    :param path:
    :return:
    '''
    try:
        shutil.rmtree(path)
    except Exception as e:
        logger.error(f"清空 {path} 出错 ：{e}")


def del_all_file(path):
    '''
    删目录下所有文件，包括子目录内
    :param path:
    :return:
    '''
    for i in os.listdir(path):
        path_file = os.sep.join([path, i])
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_all_file(path_file)


def robot_send_message(msg_type='text',message=''):
    try:
        if config.robot_url != '':
            mr = MyRequests(timeout=config.http_request_timeout)
            url = config.robot_url
            json = {
                "msg_type": msg_type,
                "content": {
                    "text": message
                }
            }
            rep = mr.run(method='post', url=url, json=json)
            if isinstance(rep, str) or rep.status_code != 200 or rep.json()['StatusMessage'] != 'success':
                return False
            return True
    except Exception as e:
        logger.error(f"{e}")
        return False



def regist_app(app_code,moniter_path):
    local_ip = config.local_ip
    local_port = config.local_port
    url = config.regist_server_url
    data = {
        'app_code':app_code,
        'moniter_path':moniter_path,
        'ip':local_ip,
        'port':local_port,
        'tag':{}}
    try:
        mr = MyRequests(timeout=3)
        rep = mr.run(url=url,method='post',json=data)
        if isinstance(rep, str) or rep.status_code != 200:
            msg = f"注册 {app_code} 失败 - 接口返回 = {rep}"
            logger.error(msg)
            return msg
        else:
            logger.info(f"注册成功--{data}")
            return True
    except Exception as e:
        logger.error(f'注册{app_code}失败:{str(e)}')
        return f'注册{app_code}失败:{str(e)}'




def str_to_dict(str):
    str = str.replace(r'\r\n','')
    str = str.replace("'", '"')
    return json.loads(str)




if "__main__" == __name__ :
    del_path(r'D:\1\2 python code\script_client\test_script\1')
