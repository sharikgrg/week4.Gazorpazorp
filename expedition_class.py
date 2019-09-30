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

    def add_pass_to_expo(self,passenger):
        if self.__list_of_passengers.append(passenger):
            return True
        else:
            return False

    def get_spaceship(self):
        return self.__spaceship

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_pass_list(self):
        return self.__list_of_passengers

    def print_list_passengers(self):
        for passenger in self.get_pass_list():
            print('Name: ' + passenger.name, 'species: ' + passenger.species, 'IDR: ' + passenger.intergalactic_dna_reg)


# an origin (probably always gazorpazorp spacestation)
# should have a destination
# spaceship assigned to it
# list of passengers