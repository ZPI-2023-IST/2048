class Node:
    def __init__(self, value: int) -> None:
        self.value = value

    def double(self) -> int:
        self.value *= 2
        return self.value

    def __repr__(self) -> str:
        return str(self.value).ljust(4)