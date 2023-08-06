from typing import Optional

import requests

from countapi.common import API_BASE, NotOKError, build_id_path


class SetResponse:
    old_value: int
    value: int

    def __init__(self, old_value: int, value: int) -> None:
        self.old_value = old_value
        self.value = value


def set_value(
    value: int,
    key: str,
    namespace: Optional[str] = None,
) -> SetResponse:
    params = {"value": value}
    res = requests.get(f"{API_BASE}/set/{build_id_path(key, namespace)}", params)

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to set counter value")

    data = res.json()
    return SetResponse(**data)
