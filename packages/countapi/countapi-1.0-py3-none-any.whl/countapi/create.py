from typing import Optional

import requests

from countapi.common import (
    API_BASE,
    NotOKError,
    filter_params,
    int_from_optional_bool,
)


class CreateResponse:
    namespace: str
    key: str
    value: int

    def __init__(self, namespace: str, key: str, value: int) -> None:
        self.namespace = namespace
        self.key = key
        self.value = value


def create_counter(
    key: Optional[str] = None,
    namespace: Optional[str] = None,
    value: Optional[int] = None,
    enable_reset: Optional[bool] = None,
    update_lower_bound: Optional[int] = None,
    update_upper_bound: Optional[int] = None,
) -> CreateResponse:
    params = filter_params(
        {
            "key": key,
            "namespace": namespace,
            "value": value,
            "enable_reset": int_from_optional_bool(enable_reset),
            "update_lowerbound": update_lower_bound,
            "update_upperbound": update_upper_bound,
        }
    )

    res = requests.get(f"{API_BASE}/create", params)

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to get info")

    data = res.json()
    return CreateResponse(**data)
