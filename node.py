class Node:
    def __init__(self, value: int) -> None:
        self.value = value

    def double(self) -> int:
        self.value *= 2
        return self.value

    def __repr__(self) -> str:
        returned = '' if self.value is None else str(self.value)
        return returned.ljust(4)
    
    def __eq__(self, other: 'Node') -> bool:
        return self.value == other.value