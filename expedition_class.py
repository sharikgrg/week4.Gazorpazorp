# a expedition should have:
class Expedition:
    def __init__(self, destination, spaceship = ' ', origin = 'Gazorpazorp'):
        self.__origin = origin
        self.__destination = destination
        self.__spaceship = spaceship
        self.__list_of_passengers = []

    def assign_spaceship(self, new_spaceship):
        self.__spaceship = new_spaceship

    def expo_details(self):
        # we want to send a dicitonary with
            # origin
            # destination
            # ship
            # passenger_list
        expo_detail = {
            'origin': self.__origin,
            'destination': self.__destination,
            'spaceship': self.__spaceship,
            'pass_list': self.__list_of_passengers
        }
        return expo_detail
# an origin (probably always gazorpazorp spacestation)
# should have a destination
# spaceship assigned to it
# list of passengers