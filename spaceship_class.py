# spaceship should have:
class Spaceship:
    def __init__(self, captain, name, signature):
        self.captain = captain
        self.__name = name
        self.__signature = signature
# captain
# name
# intergalactic_warp_drive_signature
    def identify(self):
        return self.__signature

    def identify_by_name(self):
        return self.__name

    def change_name(self, name):
        self.__name = name
