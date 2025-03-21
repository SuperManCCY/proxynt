import io
import json
import os
import uuid

from tornado.web import RequestHandler




class FileDownloadHandler(RequestHandler):
    def initialize(self, **kwargs):
        self.config = kwargs
    @staticmethod
    def generate_client_name():
        # 方法1：使用 uuid
        return f"client_{str(uuid.uuid4())[:8]}"
    def get(self):
        host = self.request.headers.get("Host")
        print(f"host:{host}")
        ws_path = self.config.get("path", "/")
        ws_password = self.config.get("password", "password")
        client_config = {
            "server": {
                "url": f"ws://{host}{ws_path}",
                "password": ws_password
            },
            "client_name": self.generate_client_name()
        }
        # 将 JSON 转换为字符串
        json_str = json.dumps(client_config, ensure_ascii=False)
        # 创建内存文件对象
        buffer = io.BytesIO(json_str.encode('utf-8'))
        # 设置响应头
        self.set_header('Content-Type', 'application/json')
        self.set_header('Content-Disposition', 'attachment; filename=config_c.json')
        # 返回文件内容
        self.write(buffer.getvalue())
        buffer.close()
