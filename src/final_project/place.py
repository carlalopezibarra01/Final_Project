import random

class Place:
    def __init__(self, place_id, host_id, city):
        self.place_id = place_id
        self.host_id = host_id
        self.city = city
        self.neighbours = []
        self.area = None
        self.rate = None
        self.price = {}
        self.occupancy = 0

    def setup(self):
        size = self.city.size
        row = self.place_id // size
        col = self.place_id % size

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < size and 0 <= nc < size:
                    self.neighbours.append(nr * size + nc)

        half = size // 2
        inv_row = size - 1 - row  # reverse Y axis
        if inv_row < half and col < half:
            self.area = 0  # bottom-left
        elif inv_row < half and col >= half:
            self.area = 1  # bottom-right
        elif inv_row >= half and col < half:
            self.area = 2  # top-left
        else:
            self.area = 3  # top-right

        rmin, rmax = self.city.area_rates[self.area]
        self.rate = random.uniform(rmin, rmax)
        self.price = {0: 900 * self.rate}

    def update_occupancy(self):
        area_rates = [p.rate for p in self.city.places if p.area == self.area]
        area_avg = sum(area_rates) / len(area_rates)
        if self.rate > area_avg:
            self.occupancy = random.randint(5, 15)
        else:
            self.occupancy = random.randint(10, 20)