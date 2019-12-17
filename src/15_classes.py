# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

place = LatLon(124, -156)
print('place: ', place.lat, place.lon)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    
    def __str__(self):
        return '{self.name} has a lattitude of {self.lat}, and a longitude of {self.lon}'.format(self=self)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# It should inherit from Waypoint so that it can gain access to name, lat, and lon)

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.diff = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    
    def __str__(self):
        return 'To find the "{self.name}" geocache, with a difficulty of {self.diff}, and a size of {self.size}, look at coordinates: {self.lat}, {self.lon}'.format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.name+ ', '+ str(waypoint.lat)+', '+ str(waypoint.lon))

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
