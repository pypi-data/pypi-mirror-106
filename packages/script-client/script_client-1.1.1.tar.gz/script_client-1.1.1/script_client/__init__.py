import os
import importlib
import configparser
from loguru import logger
from script_client import jobs
from script_client import func_map
from script_client import web_server
from script_client import run_script
from script_client.const import config as conf
from script_client.common.common_method import regist_app






print_str = '''
                               __              __                      __  __                        __     
                              /  |            /  |                    /  |/  |                      /  |    
  _______   _______   ______  $$/   ______   _$$ |_           _______ $$ |$$/   ______   _______   _$$ |_   
 /       | /       | /      \ /  | /      \ / $$   |         /       |$$ |/  | /      \ /       \ / $$   |  
/$$$$$$$/ /$$$$$$$/ /$$$$$$  |$$ |/$$$$$$  |$$$$$$/         /$$$$$$$/ $$ |$$ |/$$$$$$  |$$$$$$$  |$$$$$$/   
$$      \ $$ |      $$ |  $$/ $$ |$$ |  $$ |  $$ | __       $$ |      $$ |$$ |$$    $$ |$$ |  $$ |  $$ | __ 
 $$$$$$  |$$ \_____ $$ |      $$ |$$ |__$$ |  $$ |/  |      $$ \_____ $$ |$$ |$$$$$$$$/ $$ |  $$ |  $$ |/  |
/     $$/ $$       |$$ |      $$ |$$    $$/   $$  $$/       $$       |$$ |$$ |$$       |$$ |  $$ |  $$  $$/ 
$$$$$$$/   $$$$$$$/ $$/       $$/ $$$$$$$/     $$$$/         $$$$$$$/ $$/ $$/  $$$$$$$/ $$/   $$/    $$$$/  
                                  $$ |                                                                      
                                  $$ |                                                                      
                                  $$/                                                                          
'''



def _get_config(config_path):
    if config_path == '':
        config_path = 'config.ini'
    if not os.path.exists(config_path):
        logger.error(f"config.ini 不存在")
        return False
    try:
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8")
        conf.local_ip = config.get('conf', 'local_ip')
        conf.local_port = config.getint('conf', 'local_port')
        conf.client_name = config.get('conf', 'client_name')
        conf.regist_server_url = config.get('conf', 'regist_server_url')
        conf.heart_beat_url = config.get('conf', 'heart_beat_url')
        conf.result_url = config.get('conf', 'result_url')
        conf.http_request_timeout = config.getint('conf', 'http_request_timeout')
        conf.max_thread = config.getint('conf', 'max_thread')
        conf.max_task = config.getint('conf', 'max_task')
        conf.py_timeout = config.getint('conf', 'py_timeout')
        conf.robot_url = config.get('conf', 'robot_url')
        conf.work_path = os.getcwd()
        return True
    except Exception as e:
        logger.error(f"读取配置信息失败 {e}")
        return False


def _import_and_regist():
    if os.path.exists(os.sep.join([conf.work_path,'test_script'])):
            for root, dirs, files in os.walk(os.sep.join([conf.work_path,'test_script'])):
                for file in files:
                    if os.path.splitext(file)[1] == '.py':
                        importlib.import_module(f"test_script.{os.path.splitext(file)[0]}")
    try:
        d = func_map.fm.get_map()
        for k, v in d.items():
            for kk, vv in v.items():
                regist_app(k, kk)
        logger.info(f"app注册完成")
        return True
    except Exception as e:
        logger.error(f"app注册出错 = {e}")
        return False

def _run_threadpool():
    run_script.init_thread_pool()


def _run_job():
    jobs.init_jobs()


def _run_webserver():
    web_server.run_web_server()


def stop():
    web_server.stop_web_server()


def run(config_path=''):
    '''
    启动服务
    :param config_path: config路径，默认当前路径
    :return:
    '''
    f = os.sep.join([os.getcwd(), 'logs', 'script_client_{time}.log'])
    logger.add(f, rotation="1 days", retention="3 days")

    logger.info(print_str)
    if _get_config(config_path) and _import_and_regist():
        with open(r'pid.log', 'wb') as f:
            pid = os.getpid()
            f.write(str(pid).encode())
        _run_threadpool()
        _run_job()
        _run_webserver()









if __name__ == "__main__":
    run()
