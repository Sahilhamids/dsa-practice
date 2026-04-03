import random


class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False

        # Map stores: {value: index_in_list}
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False

        # 1. Get the index of the element we want to remove
        idx_to_remove = self.data_map[val]
        # 2. Get the value of the last element in the list
        last_element = self.data_list[-1]

        # 3. Move the last element to the index of the element to remove
        self.data_list[idx_to_remove] = last_element
        # 4. Update the map to show the last element's new position
        self.data_map[last_element] = idx_to_remove

        # 5. Remove the last element from the list and the target from the map
        self.data_list.pop()
        del self.data_map[val]

        return True

    def getRandom(self) -> int:
        # Average O(1) time complexity
        return random.choice(self.data_list)
