from Address import Address


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address: Address = to_address
        self.from_address: Address = from_address
        self.cost: int = cost
        self.track: str = track

