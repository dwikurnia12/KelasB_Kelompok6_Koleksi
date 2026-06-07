from abc import ABC, abstractmethod

class KoleksiInterface(ABC):

    @abstractmethod
    def tampilkan_info(self):
        pass

    @abstractmethod
    def get_kode(self):
        pass