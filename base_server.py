from typing import Any

from fastapi import FastAPI, APIRouter

RESPONSES_TYPE = dict[int | str, dict[str, Any]] | None


class ServerBaseRouter:
    def __init__(self):
        self.router = APIRouter()

    def _get(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'GET', r, responses)

    def _post(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'POST', r, responses)

    def _put(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'PUT', r, responses)

    def _patch(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'PATCH', r, responses)

    def _delete(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'DELETE', r, responses)

    def _connect(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'CONNECT', r, responses)

    def _head(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'HEAD', r, responses)

    def _options(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'OPTIONS', r, responses)

    def _trace(self, path: str, handler: callable, r: Any | None = None, responses: RESPONSES_TYPE = None) -> None:
        self._add(path, handler, 'TRACE', r, responses)

    def _add(self, p: str, h: callable, m: str, r: Any | None = None, rs: RESPONSES_TYPE = None) -> None:
        self.router.add_api_route(p, h, methods=[m], response_model=r, responses=rs)

    def register_handlers(self, app: FastAPI) -> None:
        self.register_handlers_with_base_url("", app)

    def register_handlers_with_base_url(self, base_url: str, app: FastAPI) -> None:
        app.include_router(self.router, prefix=base_url)
