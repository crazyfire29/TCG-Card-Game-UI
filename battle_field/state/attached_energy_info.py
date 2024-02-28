from collections import defaultdict


class AttachedEnergyInfoState:
    def __init__(self):
        # self.attached_energy_info = defaultdict(lambda: defaultdict(int))
        self.attached_energy_info = {}
        self.attached_energy_info_dictionary = {}

    # def add_race_energy_at_index(self, index, energy_type, energy_quantity):
    #     print(f"attached_energy_info: {self.attached_energy_info}")
    #     self.attached_energy_info[index][energy_type] += energy_quantity
    #
    # def remove_race_energy_at_index(self, index, energy_type, energy_quantity):
    #     self.attached_energy_info[index][energy_type] = max(0, self.attached_energy_info[index][
    #         energy_type] - energy_quantity)
    #
    # def get_race_energy_at_index(self, index, energy_type):
    #     return self.attached_energy_info[index][energy_type]

    def add_race_energy_at_index(self, index, energy_type, energy_quantity):
        if index not in self.attached_energy_info:
            self.attached_energy_info[index] = []
        print(f"add_race_energy_at_index() -> self.attached_energy_info: {self.attached_energy_info}")
        print(f"self.attached_energy_info[index]: {self.attached_energy_info[index]}")
        self.attached_energy_info[index].append((energy_type, energy_quantity))
        print(f"After self.attached_energy_info[index].append((energy_type, energy_quantity)) -> self.attached_energy_info: {self.attached_energy_info}")

    def remove_race_energy_at_index(self, index, energy_type, energy_quantity):
        if index in self.attached_energy_info:
            self.attached_energy_info[index] = [(t, q - energy_quantity) for t, q in self.attached_energy_info[index] if
                                                t != energy_type]

    def get_total_energy_at_index(self, index):
        print(f"get_total_energy_at_index -> index: {index}")
        print(f"get_total_energy_at_index.get(index, []) -> res: {self.attached_energy_info.get(index, [])}")
        print(f"self.attached_energy_info_dictionary.get(index, 0): {self.attached_energy_info_dictionary.get(index, 0)}")
        return sum(q for t, q in self.attached_energy_info.get(index, [])) + self.attached_energy_info_dictionary.get(
            index, 0)

    def get_energy_info_at_index(self, index):
        return self.attached_energy_info.get(index, [])

    def get_race_energy_at_index(self, index, energy_type):
        return sum(q for t, q in self.attached_energy_info.get(index, []) if t == energy_type)

    # def get_total_energy_at_index(self, index):
    #     return sum(self.attached_energy_info[index].values()) + self.attached_energy_info_dictionary.get(index, 0)
    #
    # def get_energy_info_at_index(self, index):
    #     return self.attached_energy_info[index]

    def add_energy_at_index(self, index, energy_quantity):
        if index in self.attached_energy_info_dictionary:
            self.attached_energy_info_dictionary[index] += energy_quantity
        else:
            self.attached_energy_info_dictionary[index] = energy_quantity

    def remove_energy_at_index(self, index, energy_quantity):
        if index in self.attached_energy_info_dictionary:
            self.attached_energy_info_dictionary[index] = max(0, self.attached_energy_info_dictionary[index] - energy_quantity)

    def get_energy_at_index(self, index):
        return self.attached_energy_info_dictionary.get(index, 0)



# class AttachedEnergyInfoState:
#     def __init__(self):
        # Dictionary는 index(0, 1, 2, 3)를 key 값으로 붙어 있는 에너지 수량(숫자)를 value로 사용
        # self.attached_energy_info_dictionary = {}

    # def add_energy_at_index(self, index, energy_quantity):
    #     if index in self.attached_energy_info_dictionary:
    #         self.attached_energy_info_dictionary[index] += energy_quantity
    #     else:
    #         self.attached_energy_info_dictionary[index] = energy_quantity
    #
    # def remove_energy_at_index(self, index, energy_quantity):
    #     if index in self.attached_energy_info_dictionary:
    #         self.attached_energy_info_dictionary[index] = max(0, self.attached_energy_info_dictionary[index] - energy_quantity)
    #
    # def get_energy_at_index(self, index):
    #     return self.attached_energy_info_dictionary.get(index, 0)

    # def add_energy_at_index(self, index, energy_type, energy_quantity):
    #     if index in self.attached_energy_info_dictionary:
    #         if energy_type in self.attached_energy_info_dictionary[index]:
    #             self.attached_energy_info_dictionary[index][energy_type] += energy_quantity
    #         else:
    #             self.attached_energy_info_dictionary[index][energy_type] = energy_quantity
    #     else:
    #         self.attached_energy_info_dictionary[index] = {energy_type: energy_quantity}
    #
    # def remove_energy_at_index(self, index, energy_type, energy_quantity):
    #     if index in self.attached_energy_info_dictionary:
    #         if energy_type in self.attached_energy_info_dictionary[index]:
    #             self.attached_energy_info_dictionary[index][energy_type] = max(
    #                 0, self.attached_energy_info_dictionary[index][energy_type] - energy_quantity)
    #
    # def get_energy_at_index(self, index):
    #     return self.attached_energy_info_dictionary.get(index, {})
