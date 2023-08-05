from . import EcoDevicesRT2
from .const import RT2_API
from .exceptions import (
    EcoDevicesRT2RequestError,
)


class Toroid:
    """Class representing the Toroid"""

    def __init__(
        self, ecort2: EcoDevicesRT2, id: int, default_value_is_consumption: bool = True
    ) -> None:
        self._ecort2 = ecort2
        self._id = id

        self._index_get_link = RT2_API["toroid"]["index"]["get"]["link"]
        self._index_get_entry = RT2_API["toroid"]["index"]["get"]["entry"] % (self._id)
        self._index_consumption_get_link = RT2_API["toroid"]["index_consumption"][
            "get"
        ]["link"]
        self._index_consumption_get_entry = RT2_API["toroid"]["index_consumption"][
            "get"
        ]["entry"] % (self._id)
        self._index_production_get_link = RT2_API["toroid"]["index_production"]["get"][
            "link"
        ]
        self._index_production_get_entry = RT2_API["toroid"]["index_production"]["get"][
            "entry"
        ] % (self._id)
        self._price_get_link = RT2_API["toroid"]["price"]["get"]["link"]
        self._price_get_entry = RT2_API["toroid"]["price"]["get"]["entry"] % (self._id)
        self._price_consumption_get_link = RT2_API["toroid"]["price_consumption"][
            "get"
        ]["link"]
        self._price_consumption_get_entry = RT2_API["toroid"]["price_consumption"][
            "get"
        ]["entry"] % (self._id)
        self._price_production_get_link = RT2_API["toroid"]["price_production"]["get"][
            "link"
        ]
        self._price_production_get_entry = RT2_API["toroid"]["price_production"]["get"][
            "entry"
        ] % (self._id)

        self._default_value_is_consumption = default_value_is_consumption
        if self._id <= 4:
            if self._default_value_is_consumption:
                self._index_get_entry = self._index_consumption_get_entry
                self._price_get_entry = self._price_consumption_get_entry
            else:
                self._index_get_entry = self._index_production_get_entry
                self._price_get_entry = self._price_production_get_entry

    def get_value(self, cached_ms: int = None) -> float:
        """Return the current Toroid status."""
        response = self._ecort2.get(self._index_get_link, cached_ms=cached_ms)
        return response[self._index_get_entry]

    @property
    def value(self) -> float:
        return self.get_value()

    def get_consumption(self, cached_ms: int = None) -> float:
        """Return the current Toroid value for consumtion, if id is between 1 and 4."""
        if self._id > 4:
            raise EcoDevicesRT2RequestError(
                "Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have consumption value."
                % self._id
            )
        response = self._ecort2.get(
            self._index_consumption_get_link, cached_ms=cached_ms
        )
        return response[self._index_consumption_get_entry]

    @property
    def consumption(self) -> float:
        return self.get_consumption()

    def get_production(self, cached_ms: int = None) -> float:
        """Return the current Toroid value for production, if id is between 1 and 4."""
        if self._id > 4:
            raise EcoDevicesRT2RequestError(
                "Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have production value."
                % self._id
            )
        response = self._ecort2.get(
            self._index_production_get_link, cached_ms=cached_ms
        )
        return response[self._index_production_get_entry]

    @property
    def production(self) -> float:
        return self.get_production()

    def get_price(self, cached_ms: int = None) -> float:
        """Return the price of toroid."""
        response = self._ecort2.get(self._price_get_link, cached_ms=cached_ms)
        return response[self._price_get_entry]

    @property
    def price(self) -> float:
        return self.get_price()

    def get_consumption_price(self, cached_ms: int = None) -> float:
        """Return the current Toroid price for consumtion, if id is between 1 and 4."""
        if self._id > 4:
            raise EcoDevicesRT2RequestError(
                "Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have price consumption value."
                % self._id
            )
        response = self._ecort2.get(
            self._price_consumption_get_link, cached_ms=cached_ms
        )
        return response[self._price_consumption_get_entry]

    @property
    def consumption_price(self) -> float:
        return self.get_consumption_price()

    def get_production_price(self, cached_ms: int = None) -> float:
        """Return the current Toroid price for production, if id is between 1 and 4."""
        if self._id > 4:
            raise EcoDevicesRT2RequestError(
                "Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have price production value."
                % self._id
            )
        response = self._ecort2.get(
            self._price_production_get_link, cached_ms=cached_ms
        )
        return response[self._price_production_get_entry]

    @property
    def production_price(self) -> float:
        return self.get_production_price()
