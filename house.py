class House:

    def __init__(self, name = '', min_slots = 0, max_slots = 0, slots_without_laptop = -1, slots_with_laptop = 0):
        self.max_slots = max_slots
        self.min_slots = min_slots
        self.slots_without_laptop = slots_without_laptop
        self.slots_with_laptop = slots_with_laptop
        self.name = str(name)
        self.slots_taken = 0
        self.students = []


    def add_student_with_laptop(self, name):
        self.slots_taken += 1
        self.slots_with_laptop -= 1
        self.students.append(str(name))
        print '{} added to {}.'.format(name, self.name)
        # print self.students

    def add_student_without_laptop(self, name):
        self.slots_taken += 1
        self.slots_without_laptop -= 1
        self.students.append(str(name))
        print '{} added to {}.'.format(name, self.name)
        # print self.students

    def print_students(self):
        print ''
        print self.name
        print ''
        for x in self.students:
            print x

    def print_students_to_file(self):
        with open(self.name + '.txt', 'w') as f:
            f.write(self.name + '\n\n')
            for x in self.students:
                f.write(str(x) + '\n')

    def __repr__(self):
        return '{}\tLaptops: {}\tPCs: {}\tMax Slots: {}'.format(self.name, str(self.slots_with_laptop),str(self.slots_without_laptop),str(self.max_slots))
