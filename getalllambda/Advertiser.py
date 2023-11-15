import json


class Price:
    def __init__(self, currency, price):
        self.currency = currency
        self.price = price

    def to_dict(self):
        return {"currency": self.currency, "price": self.price}


class Accomodation:
    def __init__(self, id, prices: Price):
        self.id = id
        self.prices = prices

    def to_dict(self):
        prices = []
        for price in self.prices:
            prices.append(price.to_dict())
        return {"id": self.id, "prices": prices}


class Advertiser:
    def __init__(self, advertiser_id, advertiser_name, accomodation: Accomodation):
        self.advertiser_id = advertiser_id
        self.advertiser_name = advertiser_name
        self.accomodation = accomodation

    def to_dict(self):
        accomodations = []
        for accomodation in self.accomodation:
            accomodations.append(accomodation.to_dict())
        return {"advertiser_id": self.advertiser_id, "advertiser_name": self.advertiser_name,
                "accomodation": accomodations}


class Advertisers:
    def __init__(self):
        self.advertisers = []

    def append_advertiser(self, advertiser: Advertiser):
        dict = advertiser.to_dict()
        self.advertisers.append(dict)

    def get_advertiser(self):
        return json.dumps(self.advertisers)
