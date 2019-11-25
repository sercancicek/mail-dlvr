from abc import ABC, abstractmethod


class FileParser(ABC):

    def __init__(self, file):
        self.file = file
        self.dictionary = {}

    @abstractmethod
    def parse_file(self):
        pass
