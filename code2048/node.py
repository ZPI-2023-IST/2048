class Node:
    def __init__(self, value: int) -> None:
        def is_power_of_two(value: int) -> bool:
            return value != 0 and (value & (value - 1)) == 0
        
        if not (value is None or (value > 0 and is_power_of_two(value))):
            raise ValueError("Node value must be a positive power of 2")
        self.value = value

    def double(self) -> int:
        self.value *= 2
        return self.value

    def __repr__(self) -> str:
        returned = '' if self.value is None else str(self.value)
        return returned.ljust(4)
    
    def __eq__(self, other: 'Node') -> bool:
        if isinstance(other, int):
            print(other)
        return self.value == other.value