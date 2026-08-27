from abc import ABC, abstractmethod


class GetScopeKeywordsPort(ABC):
    @abstractmethod
    def execute(self) -> list[str]:
        raise NotImplementedError
