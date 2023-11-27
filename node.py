class Node:
    def __init__(self, value: int) -> None:
        if value and value > 0 and value %2 != 0:
            raise ValueError("Node value must be a positive power of 2")
        self.value = value

    def double(self) -> int:
        self.value *= 2
        return self.value

    def __repr__(self) -> str:
        returned = '' if self.value is None else str(self.value)
        return returned.ljust(4)
    
    def __eq__(self, other: 'Node') -> bool:
        return self.value == other.value