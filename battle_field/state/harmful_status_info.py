class HarmfulStatusInfo:
    def __init__(self):
        self.harmful_status = {}

    def update_harmful_status(self, unit_index, harmful_status):
        print(f"update_extra_effect_of_unit: index - {unit_index}")
        print(f"current_extra_effect_info: {self.harmful_status}")
        self.harmful_status.update()
        if unit_index not in self.harmful_status.keys():
            self.harmful_status[unit_index] = []
            self.harmful_status[unit_index] = harmful_status
        else:
            self.harmful_status[unit_index] = harmful_status

        print(f"updated_extra_effect_info: {self.harmful_status}")

    def get_extra_effect_of_index(self, unit_index):
        return self.harmful_status[unit_index]

