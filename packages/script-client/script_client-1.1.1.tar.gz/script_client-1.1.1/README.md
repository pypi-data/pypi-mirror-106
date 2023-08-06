dmp-client
===================

### 环境
* python： >3.6.4
* os： any

### 安装
* pip install dmp-client

### 使用
 - 安装成功dmp_client

 - 创建config.ini ，修改字段。**名字【config.ini】不能改变，编码utf-8**

      - ```
          [conf]
          ;本机ip
          local_ip=10.10.10.101
          ;本机端口
          local_port=45678
          ;注册地址
          regist_server_url=http://10.10.10.101:8899/registry/registry
          ;心跳地址
          heart_beat_url=http://10.10.10.101:8899/registry/fameWorker
          ;测试结果回传地址
          result_url=http://xxx.xx.com/xxxx/testresult
          ;http请求超时时间（s）
          http_request_timeout=1
          ;最大线程数
          max_thread=300
          ;最大任务数
          max_task=3000
          ;测试脚本保存地址，./表示引用脚本的当前文件夹，上传的py将会按规则存放在这目录下
          test_script_dir=./
          ;脚本运行的超时时间（s），超时将会被强制杀死，回传结果为失败
          py_timeout=10
          ```

 - 创建启动脚本
   
      - 新建任意路径下任意名字的xxx.py文件，复制下边内容保存，把上边config.ini 放到xxx.py 同级目录
      
      - ```python
          import dmp_client as dc
          
          #run()函数可选参数是config文件的路径，不带参数表示config在脚本同级目录
          #或传config.ini路径
          #dc.run(r'C:\config.ini')
          dc.run()
          ```
      
- 上传测试脚本
  - url：机器的ip + config.ini里的端口号，例：http://10.2.2.101:45678/
  - 填app code，moniter path，选择py后提交
  - 提示成功后开始接收moniter发来的数据并运行对应的py