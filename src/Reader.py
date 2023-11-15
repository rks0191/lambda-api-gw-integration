from abc import ABC, abstractmethod
from src.Advertiser import Price, Accomodation, Advertiser


class Reader(ABC):
    @abstractmethod
    def _parse(self):
        pass

    def parse(self):
        content = self._parse()
        advertiser_name = content.get("name")
        advertiser_id = content.get("id")
        accomodations_array = []
        accomodations = content.get("accommodation")
        for accomodation in accomodations:
            accomodation_id = accomodation.get("id")
            accomdation_prices = accomodation.get("prices")
            prices = []
            for price in accomdation_prices:
                prices.append(Price(price.get("currency"), price.get("price")))
            accomodations_array.append(Accomodation(accomodation_id, prices))
        return Advertiser(advertiser_id, advertiser_name, accomodations_array)
