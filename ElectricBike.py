from Vehicle import Vehicle
from ScooterMixin import ScooterMixin

class ElectricBike(ScooterMixin, Vehicle):
    def __init__(self):
        super().__init__()
        self.maitenance = False
        self.counter = 0

    def set_counter(self,valor):
        if valor>=1:
            self.counter = self.counter + valor
        elif valor ==0:
            self.counter = valor

    def get_counter(self):
        print('Counter:', self.counter)

    def set_maintenance(self, valor):
        self.maitenance = valor

    def repair(self):
        if self.state == self.state_dict[4]:
            self.set_maintenance(False)
            self.set_counter(0)
            self.system_messages('* Maintenance Done !!!')
        else:
            self.system_messages('* Cannot set Maintenance out of WareHouse')

    def get_maintenance(self):
        print('Maintenance:', self.maitenance)

    def discharge(self):
        super().discharge()
        if self.battery <=15:
            self.set_counter(1)
            if self.counter >= 2:
                self.set_maintenance(True)

    def scan(self):
        if self.need_charge == True and self.state==self.state_dict[4] and self.maitenance == True:
            self.system_messages('* Battery Needed. Cannot set to Deploying\n* Maintenance Needed. Cannot set to Deploying ')
        elif self.maitenance == True and self.state==self.state_dict[4]:
            self.system_messages('* Maintenance Needed. Cannot set to Deploying')
        elif self.need_charge == True and self.state==self.state_dict[4]:
            self.system_messages('* Battery Needed. Cannot set to Deploying')
        else:
            super().scan()

    def unlock(self):
        if self.maitenance == False:
            super().unlock()
        else:
            self.system_messages('* Maintenance Needed: Vehicule Unavailable')

    def indicators(self):
        print('----------------------------')
        print('Indicators:                 ')
        print('----------------------------')
        self.get_state()
        self.get_speed()
        self.get_charge()
        self.get_battery()
        self.get_mobility()
        self.get_maintenance()
        self.get_counter()
        print('----------------------------')


