from abc import ABC, abstractmethod


class GetBlockedPatternsPort(ABC):
    @abstractmethod
    def execute(self) -> list[str]:
        raise NotImplementedError
