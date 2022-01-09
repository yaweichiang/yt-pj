from abc import ABC
from abc import abstractmethod


class Step(ABC):  # 抽象類別 至少要有1個或以上的abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):  # 處理
        pass


class StepException(Exception):  # 例外
    pass
