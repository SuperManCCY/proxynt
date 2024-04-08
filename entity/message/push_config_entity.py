from typing import List

from typing_extensions import TypedDict


class ClientData(TypedDict):
    name: str
    remote_port: int
    local_port: int
    local_ip: str
    speed_limit: float

class _ClientInfoEntity(TypedDict):
    ip: str
    host_name: str
    platform: str

class PushConfigEntity(TypedDict):
    key: str
    version: str
    config_list: List[ClientData]  # 转发配置列表
    client_name: str  # 客户端名称
    client_info: _ClientInfoEntity
