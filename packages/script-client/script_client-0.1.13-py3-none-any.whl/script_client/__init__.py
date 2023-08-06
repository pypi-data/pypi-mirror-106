import os
import configparser
from loguru import logger
from script_client import jobs
from script_client import web_server
from script_client import run_script
from script_client.const import config as conf


f = os.sep.join([os.getcwd(),'logs','dmp_client_{time}.log'])
logger.add(f, rotation="1 days", retention="10 days")


print_str = '''

######   #     #  ######         #####   #        ###  #######  #     #  ####### 
#     #  ##   ##  #     #       #     #  #         #   #        ##    #     #    
#     #  # # # #  #     #       #        #         #   #        # #   #     #    
#     #  #  #  #  ######  ##### #        #         #   #####    #  #  #     #    
#     #  #     #  #             #        #         #   #        #   # #     #    
#     #  #     #  #             #     #  #         #   #        #    ##     #    
######   #     #  #              #####   #######  ###  #######  #     #     #    

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
        conf.regist_server_url = config.get('conf', 'regist_server_url')
        conf.heart_beat_url = config.get('conf', 'heart_beat_url')
        conf.result_url = config.get('conf', 'result_url')
        conf.http_request_timeout = config.getint('conf', 'http_request_timeout')
        conf.max_thread = config.getint('conf', 'max_thread')
        conf.max_task = config.getint('conf', 'max_task')
        conf.py_timeout = config.getint('conf', 'py_timeout')
        conf.robot_url = config.get('conf', 'robot_url')
        if config.get('conf', 'test_script_dir') == './':
            conf.test_script_dir = os.getcwd()
        return True
    except Exception as e:
        logger.error(f"读取配置信息失败 {e}")
        return False


def _run_threadpool():
    run_script.init_thread_pool()


def _run_job():
    jobs.init_jobs()


def _run_webserver():
    web_server.run_web_server()


def run(config_path=''):
    logger.info(print_str)
    with open(r'pid.log', 'wb') as f:
        pid = os.getpid()
        f.write(str(pid).encode())
    if _get_config(config_path):
        _run_threadpool()
        _run_job()
        _run_webserver()


def stop():
    web_server.stop_web_server()


if __name__ == "__main__":
    run()
