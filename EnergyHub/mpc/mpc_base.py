from abc import ABC, abstractmethod
from typing import Any, Dict

class MPCBase(ABC):
    @abstractmethod
    def configure(self, config: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def optimize(self) -> None:
        pass

