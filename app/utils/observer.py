from typing import List, Protocol
class Observer(Protocol):
    def update(self, message: str) -> None:
        ...
class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
    def attach(self, observer: Observer):
        self._observers.append(observer)
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    def notify(self, message: str):
        for obs in self._observers:
            obs.update(message)