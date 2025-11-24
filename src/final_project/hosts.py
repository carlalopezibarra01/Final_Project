class Host:
    def __init__(self, host_id, place, city):
        self.host_id = host_id
        self.city = city
        self.profits = 0
        self.assets = {place.place_id}
        self.area = place.area

    def update_profits(self):
        for pid in self.assets:
            p = self.city.places[pid]
            self.profits += p.rate * p.occupancy

    def make_bids(self):
        bids = []
        owned = self.assets
        neighbors = set()

        for pid in owned:
            for n in self.city.places[pid].neighbours:
                if n not in owned:
                    neighbors.add(n)

        for pid in neighbors:
            place = self.city.places[pid]
            ask_price = list(place.price.values())[-1]

            if not self.city.use_modified_rule:
                if self.profits >= ask_price:
                    bids.append({
                        'place_id': pid,
                        'seller_id': place.host_id,
                        'buyer_id': self.host_id,
                        'spread': self.profits - ask_price,
                        'bid_price': self.profits
                    })
            else:
                if self.profits >= ask_price:
                    bids.append({
                        'place_id': pid,
                        'seller_id': place.host_id,
                        'buyer_id': self.host_id,
                        'spread': self.profits - ask_price,
                        'bid_price': self.profits
                    })

        return bids