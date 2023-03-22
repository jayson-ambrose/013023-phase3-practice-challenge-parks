from .trip import Trip

class NationalPark:

    def __init__(self, name):

        if type(name) == str:
            self._name = name

        self.trips_list = []
        self.visitors_list = []
        
        self.tot_visits =  0

    @property
    def name(self):
        return self._name

    def trips(self):
        return self.trips_list
    
    def visitors(self):
        return self.visitors_list

    def increment_total_visits (self):
        self.tot_visits = self.tot_visits + 1

    def total_visits():
        return self.tot_visits

    def best_visitor(self):
        for person in self.visitors_list:    
    
   