from abc import ABCMeta, abstractmethod


class Connection(metaclass=ABCMeta):

    @abstractmethod
    def put(self, target: str) -> bool:
        pass

    @abstractmethod
    def post(self, target: str):
        pass

    @abstractmethod
    def get(self, target: str):
        pass

    @abstractmethod
    def delete(self, target: str):
        pass
