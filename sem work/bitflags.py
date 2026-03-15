class BitFlags:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер должен быть положительным")

        self.size = size
        self.bits = [0] * size

    def add(self, index: int) -> None:
        if 0 <= index < self.size:
            self.bits[index] = 1
        else:
            print("Ошибка: индекс вне диапазона")

    def remove(self, index: int) -> None:
        if 0 <= index < self.size:
            self.bits[index] = 0
        else:
            print("Ошибка: индекс вне диапазона")

    def contains(self, index: int) -> bool:
        if 0 <= index < self.size:
            return self.bits[index] == 1
        else:
            print("Ошибка: индекс вне диапазона")
            return False

    def count(self) -> int:
        total = 0
        for bit in self.bits:
            if bit == 1:
                total += 1
        return total

    def clear(self) -> None:
        for i in range(self.size):
            self.bits[i] = 0

    def union(self, other: "BitFlags") -> "BitFlags":
        if self.size != other.size:
            raise ValueError("Размеры должны совпадать")

        result = BitFlags(self.size)

        for i in range(self.size):
            result.bits[i] = self.bits[i] | other.bits[i]

        return result

    def intersection(self, other: "BitFlags") -> "BitFlags":
        if self.size != other.size:
            raise ValueError("Размеры должны совпадать")

        result = BitFlags(self.size)

        for i in range(self.size):
            result.bits[i] = self.bits[i] & other.bits[i]

        return result

    def to_list(self):
        result = []
        for i in range(self.size):
            if self.bits[i] == 1:
                result.append(i)
        return result