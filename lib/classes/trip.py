
class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):

        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.add_trip_to_visitor()
        self.add_trip_to_national_park()
        self.add_nat_park_to_visitor()
        self.add_visitor_to_nat_park()
        self.national_park.increment_total_visits()

        Trip.all.append(self)
    
    def add_trip_to_visitor(self):
        self.visitor.trips_list.append(self)

    def add_trip_to_national_park(self):
        self.national_park.trips_list.append(self)

    def add_nat_park_to_visitor (self):
        if self.visitor not in self.national_park.visitors_list:
            self.national_park.visitors_list.append(self.visitor)

    def add_visitor_to_nat_park (self):
        if self.national_park not in self.visitor.parks_list:
            self.visitor.parks_list.append(self.national_park)

    
            
