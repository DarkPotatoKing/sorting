class House:
    # -1 slots means no limit on slots
    slots_with_laptop = 0
    slots_without_laptop = -1
    max_slots = 0
    slots_taken = 0
    students = []

    def __init__(self, max_slots = 0, slots_without_laptop = -1, slots_with_laptop = 0):
        self.max_slots = max_slots
        self.slots_without_laptop = slots_without_laptop
        self.slots_with_laptop = slots_with_laptop


    def add_student_with_laptop(self, name):
        slots_taken += 1
        slots_with_laptop -= 1
        students.append(str(name))

    def add_student_without_laptop(self, name):
        slots_taken += 1
        slots_without_laptop -= 1
        students.append(str(name))

    def __repr__(self):
        return 'Laptops: {}\tPCs: {}\tMax Slots: {}'.format(str(self.slots_with_laptop),str(self.slots_without_laptop),str(self.max_slots))
