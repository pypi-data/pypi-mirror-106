from typing import Optional

import requests

from countapi.common import API_BASE, NotOKError, build_id_path


class ValueResponse:
    value: int

    def __init__(self, value: int) -> None:
        self.value = value


def update_counter(
    amount: int,
    key: str,
    namespace: Optional[str] = None,
) -> ValueResponse:
    params = {"amount": amount}
    res = requests.get(
        f"{API_BASE}/update/{build_id_path(key, namespace)}", params
    )

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to update the counter")

    data = res.json()
    return ValueResponse(**data)


def hit_counter(
    key: str,
    namespace: Optional[str] = None,
) -> ValueResponse:
    res = requests.get(f"{API_BASE}/hit/{build_id_path(key, namespace)}")

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to hit the counter")

    data = res.json()
    return ValueResponse(**data)


def get_value(
    key: str,
    namespace: Optional[str] = None,
) -> ValueResponse:
    res = requests.get(f"{API_BASE}/get/{build_id_path(key, namespace)}")

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to get the current count")

    data = res.json()
    return ValueResponse(**data)
