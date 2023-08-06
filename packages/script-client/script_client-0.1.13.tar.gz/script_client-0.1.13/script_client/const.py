


class Config:
    def __init__(self):
        self.local_ip='127.0.0.1'
        self.local_port = 7788
        self.regist_server_url = r'https://www.baidu.com/'
        self.heart_beat_url = r'https://www.baidu.com/'
        self.result_url = r'https://www.baidu.com/'
        self.http_request_timeout = 1
        self.max_thread = 100
        self.max_task = 2000
        self.test_script_dir = r'D:\1\ts'
        self.py_timeout = 15
        self.robot_url = ''
        pass


config = Config()
