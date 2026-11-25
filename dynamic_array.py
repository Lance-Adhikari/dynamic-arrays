class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        # Capacity includes unused slots; size counts stored values.
        self.arr = [None] * self.capacity

    def push_back(self, val):
        if self.size == self.capacity:
            # Double the storage when all available slots are occupied.
            new_arr = [None] * (self.capacity * 2)

            # Copy existing values in order before replacing the old storage.
            for i in range(self.size):
                new_arr[i] = self.arr[i]

            self.arr = new_arr
            self.capacity = self.capacity * 2

        # Place the new value in the first unused slot.
        self.arr[self.size] = val
        self.size = self.size + 1


def main():
    array = DynamicArray()
    array.push_back(10)
    array.push_back(20)
    array.push_back(30)
    array.push_back(40)
    array.push_back(50)

    print(array.arr)
    print("size =", array.size)
    print("capacity =", array.capacity)


if __name__ == "__main__":
    main()
