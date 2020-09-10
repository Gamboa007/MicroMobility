
class Vehicle:
    def __init__(self):
        self.state_dict = {0:'Locked',1:'Unlocked',2:'In-Ride',3:'In-Transit',4:'In-WareHouse',5:'Deploying'}
        self.state = self.state_dict[0]
        self.current_speed = 0
        self.speed_range = list (range(1,51))
        self.mobility = 0

    def set_speed(self, val):
        if self.state==self.state_dict[1] or self.state==self.state_dict[2]:
            self.current_speed = val
            if val <= 0:
                self.system_messages('* Vehicule stopped ')
                self.state = self.state_dict[1]
            elif val not in self.speed_range:
                self.state = self.state_dict[2]
                self.set_mobility(1)
                self.current_speed =50
                self.system_messages('* Speed Limit Reached: Max 50km/h ')
            else:
                self.state = self.state_dict[2]
                self.set_mobility(1)
        else:
            self.system_messages('* Invalid State')

    def get_speed(self):
        print('Current Speed:',self.current_speed)

    def set_state(self, sta):
        self.state = self.state_dict[sta]

    def set_mobility(self, mobi):
        self.mobility = mobi

    def get_mobility(self):
        print('Mobility:', self.mobility)

    def get_state(self):
        print('Current State:',self.state)

    def lock(self):
        pass

    def unlock(self):
        pass

    def scan(self):
        pass

    def indicators(self):
        pass

    def system_messages(self, message):
        print('System Messages:   ')
        print(message)













