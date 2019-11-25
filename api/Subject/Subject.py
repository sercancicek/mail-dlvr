from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self, id, campaign):
        pass
