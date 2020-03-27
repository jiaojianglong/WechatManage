FROM python:3.5

COPY ./requirements /usr/local/bin/WechatManage/requirements
WORKDIR /usr/local/bin/WechatManage/
RUN pip install -r requirements -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./wxclient/ /usr/local/bin/WechatManage/wxclient
COPY ./settings.py /usr/local/bin/WechatManage/settings.py
COPY ./runserver.py /usr/local/bin/WechatManage/runserver.py

CMD ["python", "/usr/local/bin/WechatManage/runserver.py"]
