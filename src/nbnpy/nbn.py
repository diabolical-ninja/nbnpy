"""Client for the unofficial NBN API."""

from typing import Optional

from httpx import get


class NBN:
    """Interacts with NBN's unofficial API."""

    def __init__(self) -> None:
        """Sets base values required for API calls."""
        self.nbn_base_url = "https://places.nbnco.net.au/places"
        self.headers = {
            "Referer": "https://www2.nbnco.com.au/residential/learn/rollout-map"
        }

    def get_location_ids_from_lat_long(
        self, latitude: float, longitude: float
    ) -> Optional[dict]:
        """Returns NBN location ID's present near the lat & long combination.

        Location ID looks like LOC000000000000

        Args:
            latitude (float): Address latitude
            longitude (float): Address longitude

        Returns:
            dict: Locations & their ID's for addresses near the lat/long pairs

        Examples:
            >>> from nbnpy.nbn import NBN
            >>> nbn_client = NBN()
            >>> location_ids = nbn_client.get_location_ids_from_lat_long(
                    -37.80978345290123, 144.96518949578348
                )
            >>> bool(location_ids)
        """
        url = f"{self.nbn_base_url}/v1/nearby"

        params: dict = {
            "lat": latitude,
            "lng": longitude,
            "source": "website_rollout_map",
        }

        response = get(url=url, params=params, headers=self.headers)
        response_dict: dict = response.json()

        return response_dict

    def location_information(self, location_id: str) -> Optional[dict]:
        """Get connection type & details for given location.

        Args:
            location_id (str): NBN Location ID

        Returns:
            dict: Information regarding the connection details & type

        Examples:
            >>> from nbnpy.nbn import NBN
            >>> nbn_client = NBN()
            >>> location_info = nbn_client.location_information("LOC000175860243")
            >>> bool(location_info)
        """
        url = f"{self.nbn_base_url}/v2/details/{location_id}"

        params = {"source": "website_rollout_map"}

        response = get(url=url, params=params, headers=self.headers)
        response_dict: dict = response.json()

        return response_dict

    def get_location_ids_from_address(self, address: str) -> Optional[dict]:
        """Returns NBN location ID's present near the given address.

        Location ID looks like LOC000000000000

        Args:
            address (str): Location address

        Returns:
            dict: Locations & their ID's the address

        Examples:
            >>> from nbnpy.nbn import NBN
            >>> nbn_client = NBN()
            >>> location_ids = nbn_client.get_location_ids_from_address(
                    "1 Flinders Street, Melbourne VIC"
                )
            >>> bool(location_ids)
        """
        url = f"{self.nbn_base_url}/v1/autocomplete"

        params = {"query": address}

        response = get(url=url, params=params, headers=self.headers)
        response_dict: dict = response.json()

        return response_dict
