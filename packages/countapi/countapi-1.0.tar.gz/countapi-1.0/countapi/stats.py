import requests

from countapi.common import API_BASE, NotOKError


class StatsResponse:
    keys_created: int
    keys_updated: int
    requests: int
    version: str

    def __init__(
        self,
        keys_created: int,
        keys_updated: int,
        requests: int,
        version: str,
    ) -> None:
        self.keys_created = keys_created
        self.keys_updated = keys_updated
        self.requests = requests
        self.version = version


def get_stats() -> StatsResponse:
    res = requests.get(f"{API_BASE}/stats")

    if res.status_code != 200:
        raise NotOKError(res.status_code, "failed to get global CountAPI stats")

    data = res.json()
    return StatsResponse(**data)
