from Vehicle import Vehicle

class Bicycle(Vehicle):

    def __init__(self):
        super().__init__()
        self.maintenance = False
        self.counter = 0

    def set_maintenance(self,mtt):
        self.maintenance = mtt

    def set_counter(self, valor):
        if valor==1:
            self.counter = self.counter + valor
            if self.counter >=3:
                self.set_maintenance(True)
        elif valor ==0:
            self.counter = 0

    def get_counter(self):
        print('Counter:', self.counter)

    def get_maintennce(self):
        print('Maintenance:', self.maintenance)

    def repair(self):
        if self.state == self.state_dict[4]:
            self.set_maintenance(False)
            self.system_messages('* Maintenance Done !!!')
        else:
            self.system_messages('* Not possible maintenance out of WareHouse')

    def unlock(self):
        if self.maintenance == False:
            if self.maintenance == False and self.state == self.state_dict[0]:
                self.state=self.state_dict[1]
                self.system_messages('* Vehicle Get Unlocked')
        elif self.maintenance == True:
            self.system_messages('* Maintenance Required. Unavailable')

    def lock(self):
        if self.current_speed == 0:
            if self.mobility == 1 and self.state == self.state_dict[1]:
                self.state = self.state_dict[0]
                self.set_counter(1)
                self.set_mobility(0)
                self.system_messages('* Vehicle Get Locked ')
            elif self.mobility == 0 and self.state == self.state_dict[1]:
                self.state = self.state_dict[0]
                self.system_messages('* Vehicle Get Locked ')
            elif self.maintenance == True:
                self.system_messages('* Maintenance Required. Unavailable ')
            else:
                self.system_messages('* Stop Before Locking ')
        else:
            self.system_messages('* Stop Before Locking ')

    def indicators(self):
            print('----------------------------')
            print('Indicators:                 ')
            print('----------------------------')
            self.get_state()
            self.get_speed()
            self.get_counter()
            self.get_maintennce()
            self.get_mobility()
            print('----------------------------')

    def scan(self):
        if self.state == self.state_dict[0] and self.maintenance == True:
            self.state = self.state_dict[3]
            self.system_messages('* In- Transit to WareHouse')
        elif self.state == self.state_dict[3]:
            self.state = self.state_dict[4]
            self.system_messages('* Vehicule in WareHouse')
        elif self.state == self.state_dict[4] and self.maintenance == False:
            self.state = self.state_dict[5]
            self.system_messages('* Vehicule Ready To Be Used ')
        elif self.state == self.state_dict[5]:
            self.state = self.state_dict[0]
            self.system_messages('* Vehicule in Street ')



