# import all classes here
from passenger_class import *
from spaceship_class import *
from expedition_class import *

# create objects here
    # generate 6 passengers
passenger1 = Passenger('Vish', 'Which', '007')
passenger2 = Passenger('Mous', 'martian', '684')
passenger3 = Passenger('David', 'Which', '666')
passenger4 = Passenger('Lennox', 'Marching', '777')
passenger5 = Passenger('Dan', 'Pluton', '584')
passenger6 = Passenger('chewie', 'Wookie', '657')


    # generate 3 spaceships
ship_1 = Spaceship('Morgan', 'RPS', 'XYZ1015')
ship_2 = Spaceship('Marvel', 'Dissapointos', 'GPO1345')
ship_3 = Spaceship('Sparrow', 'Black Pearl', 'BP56070')


    # generate 3 expeditions
expo1 = Expedition('Mars', ship_3)
expo2 = Expedition('Death star', ship_2)
expo3 = Expedition('Final Destination', ship_1)
        # keep lists of generated expedition (empty list of expedition)
        # assign a spacecraft to each one
            # should be able to assign on creation of object or
            # should be able to assign post-facto


    # Assign each expedition 2 passengers (append)
expo1.add_pass_to_expo(passenger1)
expo1.add_pass_to_expo(passenger2)
expo2.add_pass_to_expo(passenger3)
expo2.add_pass_to_expo(passenger4)
expo3.add_pass_to_expo(passenger5)
expo3.add_pass_to_expo(passenger6)
print(expo1.expo_details())
print(expo1.expo_details()['pass_list'][0].species)

    # iterate over list of expeditions and print


    # iterate over list of expeditions and print
        # iterare over list of passenger objects
            # print out passenger details


# create while loop here
    # Use input to get user input and generate object dynamically
# - as a user i can create passengers
# - as a user i can list all expeditions
# - as a user i can add a passenger to a expedition
# - as a user i can list passengers in one expedition
