from Vehicle import Vehicle

class Scooter(Vehicle):
    def __init__(self):
        super().__init__()
        self.battery = 100
        self.need_charge = False
        self.mobility = 0

    def set_battery(self, percent):
        if percent <= 15:
            self.set_need_charge(True)
            self.battery = percent
        else:
            self.battery = percent
            self.set_need_charge(False)

    def set_need_charge(self, state):
        self.need_charge = state

    def get_battery(self):
        print('Baterry level:', self.battery)

    def get_charge(self):
        print('Need Charge:', self.need_charge)

    def discharge(self):
        self.battery = self.battery - 17
        if self.battery < 16:
            self.set_need_charge(True)

    def recharge(self):
        if self.state == self.state_dict[4]:
            self.set_battery(100)
        else:
            self.system_messages('* Not possible to charge out of WareHouse')

    def lock(self):
        if self.current_speed == 0:
            if self.mobility == 1 and self.state == self.state_dict[1]:
                self.state = self.state_dict[0]
                self.discharge()
                self.set_mobility(0)
                self.system_messages('* Vehicle Get Locked')
            elif self.mobility == 0 and self.state == self.state_dict[1]:
                self.state = self.state_dict[0]
                self.system_messages('* Vehicle Get Locked')
            else:
                self.system_messages('*  Stop Before Locking')
        else:
            self.system_messages('* Stop Before Locking')

    def unlock(self):
        if self.battery > 15 and self.state == self.state_dict[0]:
            self.set_state(1)
            self.system_messages('* Vehicle Get Unlocked ')
        elif self.battery <= 15:
            self.system_messages('* Low Battery: Vehicule Unavailable ')
        else:
            self.system_messages('* Invalid Action')

    def scan(self):
        if self.state == self.state_dict[0] and self.need_charge == True:
            self.state = self.state_dict[3]
        elif self.state == self.state_dict[3]:
            self.state = self.state_dict[4]
        elif self.state == self.state_dict[4] and self.need_charge == False:
            self.state = self.state_dict[5]
            self.system_messages('* Vehicule Ready To Be Used')
        elif self.state == self.state_dict[5]:
            self.state = self.state_dict[0]
            self.system_messages('* Vehicule in Street')


    def indicators(self):
        print('----------------------------')
        print('Indicators:                 ')
        print('----------------------------')
        self.get_state()
        self.get_speed()
        self.get_charge()
        self.get_battery()
        self.get_mobility()
        print('----------------------------')
