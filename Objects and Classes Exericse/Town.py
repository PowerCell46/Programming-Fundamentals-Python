class Town:
    def __init__(self, name_of_the_town):
        self.name = name_of_the_town

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'
