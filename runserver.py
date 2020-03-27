

from tornado.ioloop import IOLoop
from  wxclient.client import TcpClient
import settings


if __name__ == '__main__':
    tcp_client = TcpClient(
        settings.WXBot.get("host"),
        settings.WXBot.get("accept_port"),
        settings.WXBot.get("send_port"),
        )
    tcp_client.start_accept()
    tcp_client.start_send()
    IOLoop.instance().start()