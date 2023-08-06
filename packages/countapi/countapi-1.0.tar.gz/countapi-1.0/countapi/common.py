from typing import Any, Dict, Optional

API_BASE = "https://api.countapi.xyz"


def filter_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """filter_params removes pairs from params where value is None."""

    out: Dict[str, Any] = {}

    for key, value in params.items():
        if value is not None:
            out[key] = value

    return out


def int_from_optional_bool(val: Optional[bool]) -> Optional[int]:
    if val is None:
        return None

    return 1 if val is True else 0


def build_id_path(key: str, namespace: Optional[str] = None):
    if namespace is not None:
        return f"{namespace}/{key}"
    return key


class NotOKError(RuntimeError):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(f"{message} [status {status_code}]")


class ErrorResponse:
    error: str

    def __init__(self, error) -> None:
        self.error = error
