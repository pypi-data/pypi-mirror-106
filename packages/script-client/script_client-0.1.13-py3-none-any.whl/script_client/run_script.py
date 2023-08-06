
import queue
import requests
import threading
import subprocess
from loguru import logger
from threading import Timer
from script_client.const import config
from script_client.common.my_requests import MyRequests
from script_client.common.common_method import replace_str



# 用来表示终止的特殊对象
sentinel = object()
# 先进先出
q = None


def _send_resurl(data):
    url = config.result_url
    json = {
        'app_code': data['app_code'],
        'moniter_path': data['moniter_path'],
        'result': (1 if data['exit_code'] == 0 else 0),#0失败，1通过
        'result_body': {
            'stdout': replace_str((data['stdout'])),
            'stderr': replace_str((data['stderr']))
        }
    }
    logger.debug(f"{json}")
    mr = MyRequests(config.http_request_timeout)
    try:
        rep = mr.run(url=url, method='post', json=json)
        if isinstance(rep, requests.models.Response):
            if rep.status_code != 200:
                logger.error(f"回传脚本验证结果失败 - status_code = {rep.status_code}")
        else:
            logger.error(f"回传脚本验证结果失败 -{rep}")
    except Exception as e:
        logger.error(f'回传脚本验证结果失败:{e}')
    pass


def _timeout_callback(p):
    try:
        p.kill()
        logger.warning(f"timeout, killed --> {p.pid}")
    except Exception as error:
        logger.error(error)


def _run(data,shell=False,stdin=subprocess.PIPE,
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=config.py_timeout):
    _process = subprocess.Popen(
        data['cmd'],shell=shell,
        stdin=stdin,stdout=stdout,stderr=stderr
    )
    _timer = Timer(timeout, _timeout_callback, [_process])
    _timer.start()
    try:
        stdout, stderr = _process.communicate()
        # logger.warning(type(stdout))
        # logger.warning(stderr)
        exit_code = _process.returncode
        data = {
            'exit_code':exit_code,
            'stdout': str(stdout, encoding = "utf-8"),
            'stderr': str(stderr, encoding = "utf-8"),
            'app_code': data['app_code'],
            'moniter_path': data['moniter_path'],
        }
        # exit_code ：0=ok,1=err
        _send_resurl(data)
    except Exception as e:
        logger.error(f"process过程出错：{e}")
    finally:
        _timer.cancel()


class MyThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start()

    def run(self):
        while True:
            try:
                # block=False 没任务弹异常，=True且有timeout等timeout，过了弹异常，没timeout死等
                data = self.queue.get()
                if data is sentinel:
                    self.queue.put(sentinel)
                    break
                _run(data)
                self.queue.task_done()
            except Exception as e:
                logger.info(f"{e}")



class MyThreadPool():
    def __init__(self, queue, size):
        self.queue = queue
        self.pool = []
        for i in range(size):
            self.pool.append(MyThread(queue))




def init_thread_pool():
    global q
    q = queue.Queue(config.max_task)
    MyThreadPool(queue=q, size=config.max_thread)
    logger.info(f"线程池初始化完成...")




if __name__ == '__main__':
    pass