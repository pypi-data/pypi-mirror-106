from .controller import MLDaliController
import time

class MLDaliLight():

    def __init__(self, address):
        self.address = address
        self._controller = MLDaliController.register(self)
        self.is_on = False
    
    async def turn_on(self):
        cmd = bytearray([0x01, (self.address*2)+1, 5, 0xC1])
        time.sleep(.1) #This delay ensures that the command doesn't collapse with other commands being send on the bus
        await self._controller.sendCmd(cmd)

    
    async def turn_off(self):
        cmd = bytearray([0x01, (self.address*2)+1, 0, 0xC1])
        time.sleep(.1)
        await self._controller.sendCmd(cmd)
    
    def status_update(self, rx):
        print(f"Component at address {self.address} received status_update: {rx}")
        if rx[2:3] == b'\x05':
            self.is_on = True
        elif rx[2:3] == b'\x00':
            self.is_on = False