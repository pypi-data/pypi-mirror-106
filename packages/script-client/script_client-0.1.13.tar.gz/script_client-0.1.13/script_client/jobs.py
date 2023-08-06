
import os
from loguru import logger
import requests
from script_client.common.my_requests import MyRequests
from script_client.common.common_method import robot_send_message
from apscheduler.schedulers.background import BackgroundScheduler
from script_client.const import config


scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval',id='heart_beat', seconds=30)
def send_heart_beat():
    try:
        app_list = next(os.walk(config.test_script_dir))[1]
        if app_list:
            mr = MyRequests(timeout=config.http_request_timeout)
            for app in app_list:
                if app == 'logs':
                    continue
                url = config.heart_beat_url
                data = {"app_code":str(app)}
                rep = mr.run(url=url, method='post',json=data)
                if isinstance(rep, requests.models.Response):
                    if rep.status_code != 200 :
                        msg = f"心跳发送失败 - app = {str(app)} status_code = {rep.status_code}"
                        logger.error(msg)
                        robot_send_message(message=msg)
                else:
                    logger.error(f"心跳发送失败 app = {str(app)} ， {rep}")
                    robot_send_message(message='心跳发送失败')
    except Exception as e:
        logger.error(e)



def init_jobs():
    try:
        scheduler.start()
        logger.info(f"scheduler启动完成...")
    except Exception as e:
        logger.error(f"job err =  {e}")