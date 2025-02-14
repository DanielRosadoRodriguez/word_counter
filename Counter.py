from abc import ABC, abstractmethod

class Counter(ABC):

    @abstractmethod
    def get_number_of_lines():
        pass
