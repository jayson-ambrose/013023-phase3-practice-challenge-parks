class Visitor:

    def __init__(self, name):

        if type(name) == str:
            self._name = name

        self.trips_list = []
        self.parks_list = []

    @property
    def name(self):
        return self._name
    
    def trips(self):
        return self.trips_list

    def nationalparks(self):
        return self.parks_list

    def create_trip(self,  national_park, start_date, end_date):

        from .trip import Trip
        Trip(self, national_park, start_date, end_date)