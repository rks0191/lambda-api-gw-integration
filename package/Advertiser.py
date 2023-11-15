class Price:
    def __init__(self, currency, price):
        self.currency = currency
        self.price = price


class Accomodation:
    def __init__(self, id, prices):
        self.id = id
        self.prices = prices


class Advertiser:
    def __init__(self, advertiser_id, advertiser_name, accomodation):
        self.advertiser_id = advertiser_id
        self.advertiser_name = advertiser_name
        self.accomodation = accomodation
