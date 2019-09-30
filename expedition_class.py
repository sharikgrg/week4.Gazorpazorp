# a expedition should have:
class Expedition:
    def __init__(self, destination, spaceship, origin = 'Gazorpazorp'):
        self.origin = origin
        self.destination = destination
        self.spaceship = spaceship
        self.list_of_passengers = []

# an origin (probably always gazorpazorp spacestation)
# should have a destination
# spaceship assigned to it
# list of passengers