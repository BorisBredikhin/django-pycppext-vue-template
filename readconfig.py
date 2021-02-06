from typing import Tuple, Optional

import yaml

class Addr:
    host: str
    port: int
    def __init__(self, d):
        self.__dict__ = d


class AppConfig:
    db: str
    addr: Addr
    secret_key: str
    def __init__(self, d):
        self.__dict__ = d
        self.addr = Addr(self.addr)


_config: Optional[AppConfig] = None

def load_config(fd) -> AppConfig:
    global _config
    _config = AppConfig(yaml.load(fd, Loader=yaml.FullLoader))
    return _config

def get_config() -> Tuple[Optional[AppConfig], bool]:
    if _config is None:
        return None, True
    return _config, False
