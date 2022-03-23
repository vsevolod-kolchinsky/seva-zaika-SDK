from typing import Any, Generator, Iterable, Optional

import requests

from .exceptions import EntityImproperlyConfigured, LotrApiError


class BaseClient:
    """API client base class"""

    base_url = "https://the-one-api.dev/v2"

    def __init__(self, api_key: str) -> None:
        """Initialize client"""
        self.api_key = api_key

    def _get(self, endpoint_url: str, **kwargs) -> dict:
        """Place API call request and handle errors"""
        params = self.coerce_params(kwargs)
        rv = requests.get(
            endpoint_url, headers=self._get_request_headers(), params=params
        )
        if rv.status_code >= 400:
            raise LotrApiError(rv.text, status_code=rv.status_code)
        return rv.json()

    def _get_request_headers(self) -> dict:
        """Request authorization headers"""
        return {"Authorization": f"Bearer {self.api_key}"}

    def coerce_param_name(self, param_name: str) -> str:
        """Translate kwarg param name into API param name"""
        components = param_name.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    def coerce_param(self, param_name: str, modifier: str) -> str:
        """Translate param into query API param"""
        name = self.coerce_param_name(param_name)
        if modifier == "ne":
            # not equal
            return f"{name}!"
        elif modifier == "gt":
            # greater than
            return f"{name}>"
        elif modifier == "lt":
            # less than
            return f"{name}<"
        elif modifier == "gte":
            # greater than or equal to
            return f"{name}>="
        elif modifier == "lte":
            # less than or equal to
            return f"{name}<="
        else:
            raise ValueError(f"Unsupported query param modifier {modifier!r}")

    def coerce_params(self, native_kwargs: dict) -> dict:
        """Translate kwargs into filtering params"""
        rv = {}
        for key, val in native_kwargs.items():
            if "__" in key:
                param_name, modifier = key.split("__", 1)
                param = self.coerce_param(param_name, modifier)
            else:
                param = key
            rv[param] = val
        return rv

    def get_endpoint_url(
        self,
        endpoint: str,
        item_id: Optional[str] = None,
        sub_endpoint: Optional[str] = None,
    ) -> str:
        """Build endpoint URL"""
        url_parts = [self.base_url, "/", endpoint]
        if item_id is not None:
            url_parts.extend(["/", item_id])
        if sub_endpoint is not None:
            url_parts.extend(["/", sub_endpoint])
        return "".join(url_parts)


class BaseEntityApi:
    """Base class to describe API entity"""

    def __init__(self, api_client) -> None:
        self._api_client = api_client
        self._filters: dict = {}
        self._request_params: dict = {}
        self._limit: Optional[int] = None
        self._page: Optional[int] = None
        self._offset: Optional[int] = None
        self._sorting: dict = {}

    def fetch(self) -> Iterable[Any]:
        """Get list of fetched items"""
        return list(self.fetch_all())

    def fetch_all(self) -> Generator:
        """Fetch data from API"""
        # if filters is empty - fetch all entities
        if not self._filters:
            getter = getattr(self._api_client, self.get_entity_attr("entites_getter"))
            rv = getter(**self.get_request_params())
        elif "_id" in self._filters:
            getter = getattr(self._api_client, self.get_entity_attr("entity_getter"))
            rv = getter(self._filters["_id"])
        else:
            getter = getattr(self._api_client, self.get_entity_attr("entites_getter"))
            rv = getter(**self._filters)

        entity_model = self.get_entity_model()
        for item in rv.get("docs", []):
            yield entity_model(api_client=self._api_client, **item)

    def fetch_one(self) -> Any:
        """Fetch single entity"""
        return next(self.fetch_all())

    def filter(self, **kwargs) -> Any:
        """Set query filters"""
        for key, val in kwargs.items():
            self._filters[key] = val
        return self

    def get_entity_attr(self, attr_name: str) -> Any:
        """Get attribute after validation"""
        if not hasattr(self, attr_name):
            raise EntityImproperlyConfigured(
                f"{self.__class__.__name__} missing the {attr_name!r} property"
            )
        return getattr(self, attr_name)

    def get_entity_model(self) -> Any:
        """Get results model"""
        return self.get_entity_attr("entity_model")

    def get_request_params(self) -> dict:
        """Get request filters and pagination params"""
        params: dict = {}
        if self._limit is not None:
            params["limit"] = self._limit
        if self._offset is not None:
            params["offset"] = self._offset
        if self._page is not None:
            params["page"] = self._page
        for key, val in self._sorting.items():
            params["sort"] = f"{key}:{val}"
        return params

    def limit(self, limit: int) -> Any:
        """Limit query"""
        self._limit = limit
        return self

    def offset(self, offset: int) -> Any:
        """Get data with specified offset

        Limit default is 10
        """
        self._offset = offset
        return self

    def page(self, page: int) -> Any:
        """Get specific page

        Limit default is 10
        """
        self._page = page
        return self

    @property
    def query(self) -> Any:
        """Build fetch query"""
        return self

    def sort(self, **kwargs) -> Any:
        """Set query sorting"""
        for key, val in kwargs.items():
            if val.lower() not in ("asc", "desc"):
                raise ValueError(f"Unsupported sorting: {val!r}")
            self._sorting[key] = val
            break  # supporting only one sorting field
        return self
