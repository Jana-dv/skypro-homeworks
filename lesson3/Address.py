class Address:
    
    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment
    
    def to_string(self):
        return self.index + " " + self.city + " " + self.street + " " + self.building + " - " + str(self.apartment)