# The adapter design pattern specifically makes incompatible interfaces
# work together by transforming the interface of one class into the format expected by another.

from abc import ABC, abstractmethod

class UKPlugInterface(ABC):
    @abstractmethod
    def electricty_220v(self):
        pass


class UKPlug(UKPlugInterface):
    def electricty_220v(self):
        print('220 volts')


class USSocketInterface(ABC):
    @abstractmethod
    def electricty_110v(self):
        pass


class USSocket(USSocketInterface):
    def electricty_110v(self):
        print('110 volts')


class UKToUSAdapter(UKPlugInterface):
    def __init__(self) -> None:
        self.us_socket = USSocket()
    
    def electricty_220v(self):
        self.us_socket.electricty_110v()

uk_plug = UKPlug()
uk_plug.electricty_220v()
us_socket = USSocket()
us_socket.electricty_110v()

adapter = UKToUSAdapter()
adapter.electricty_220v()
    
