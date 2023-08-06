from datetime import datetime as DateTime
from typing import Optional

import requests

from countapi.common import API_BASE, NotOKError, build_id_path, filter_params


class InfoResponse:
    namespace: str
    key: str
    ttl: int
    value: int
    enable_reset: bool
    update_upper_bound: int
    update_lower_bound: int
    created_at: DateTime

    def __init__(
        self,
        namespace: str,
        key: str,
        ttl: int,
        value: int,
        enable_reset: bool,
        update_upperbound: int,
        update_lowerbound: int,
        created: int,  # milliseconds since epoch
    ) -> None:
        self.namespace = namespace
        self.key = key
        self.ttl = ttl
        self.value = value
        self.enable_reset = enable_reset
        self.update_upper_bound = update_upperbound
        self.update_lower_bound = update_lowerbound
        self.created_at = DateTime.utcfromtimestamp(created / 1000)


def get_info(key: str, namespace: Optional[str] = None) -> InfoResponse:
    params = filter_params({"namespace": namespace})

    res = requests.get(f"{API_BASE}/info/{build_id_path(key, namespace)}", params)

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to get info")

    data = res.json()
    return InfoResponse(**data)
