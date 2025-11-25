import pandas as pd
import random
from .place import Place
from .hosts import Host

class City:
    def __init__(self, size, area_rates):
        self.size = size
        self.area_rates = area_rates
        self.step = 0
        self.places = []
        self.hosts = []
        self.use_modified_rule = False
        self.history_rates = {0: [], 1: [], 2: [], 3: []}

    def initialize(self):
        for pid in range(self.size * self.size):
            host_id = pid
            place = Place(pid, host_id, self)
            self.places.append(place)

        for p in self.places:
            p.setup()

        for p in self.places:
            h = Host(p.host_id, p, self)
            self.hosts.append(h)

        self.record_rates()

    def record_rates(self): #necessary for graph 2 version 1
        areas = {0: [], 1: [], 2: [], 3: []}
        for p in self.places:
            areas[p.area].append(p.rate)
        for a in areas:
            avg = sum(areas[a]) / len(areas[a])
            self.history_rates[a].append(avg)

    def approve_bids(self, bids):
        if not bids:
            return []

        df = pd.DataFrame(bids)
        df = df.sort_values(by='spread', ascending=False)

        bought = set()
        sold = set()
        approved = []

        for _, bid in df.iterrows():
            pid = int(bid['place_id'])
            buyer = int(bid['buyer_id'])
            seller = int(bid['seller_id'])

            if buyer not in bought and pid not in sold:
                approved.append(bid)
                bought.add(buyer)
                sold.add(pid)

        return approved

    def execute_transactions(self, transactions):
        for t in transactions:
            pid = int(t['place_id'])
            buyer = int(t['buyer_id'])
            seller = int(t['seller_id'])
            price = t['bid_price']

            place = self.places[pid]
            buyer_host = self.hosts[buyer]
            seller_host = self.hosts[seller]

            buyer_host.profits -= price
            seller_host.profits += price

            seller_host.assets.remove(pid)
            buyer_host.assets.add(pid)

            place.host_id = buyer
            place.price[self.step] = price

            if self.use_modified_rule:
                place.rate = place.rate * random.uniform(0.95, 1.15)

    def clear_market(self):
        bids = []
        for h in self.hosts:
            bids.extend(h.make_bids())

        approved = self.approve_bids(bids)

        if approved:
            self.execute_transactions(approved)

        return approved

    def iterate(self):
        self.step += 1

        for p in self.places:
            p.update_occupancy()

        for h in self.hosts:
            h.update_profits()

        self.clear_market()
        self.record_rates() #necessary for graph 2 version 1