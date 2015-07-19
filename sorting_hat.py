from __future__ import division
from house import House
import math
import random

class SortingHat:    

    def __init__(self):
        self.load_config()
        self.assign_house_slots()
        self.sort_students()

    def load_config(self):
        lines = []
        with open('config.cfg', 'r') as f:
            lines = [x.strip() for x in f.readlines()]

        config = dict()
        for x in lines:
            temp = x.split(':')
            key = temp[0]
            val  = temp[1]
            config[key] = val

        self.num_students = int(config['num_students'])

    def assign_house_slots(self):
        max_students_per_house = int(math.ceil(self.num_students / 4))

        # purely laptop class
        self.slytherin = House('Slytherin', max_students_per_house, 0, -1)

        # 10 slots without laptop, the rest with laptops
        self.ravenclaw = House('Ravenclaw', max_students_per_house, 10, -1)

        # normal labs
        self.hufflepuff = House('Hufflepuff', max_students_per_house)
        self.gryffindor = House('Gryffindor', max_students_per_house)

        self.houses = [self.slytherin, self.ravenclaw, self.hufflepuff, self.gryffindor]
        
        # for x in self.houses:
        #     print x

    def sort_students(self):
        while True:
            self.display_art()

            name = raw_input('Enter your name:\t')
            has_laptop = raw_input('Can you bring a laptop (y/n):\t').lower()
            has_laptop = has_laptop == 'y' or has_laptop == 'yes'
            # print has_laptop

            if has_laptop:
                self.assign_student_with_laptop(name)
            else:
                self.assign_student_without_laptop(name)

            if raw_input('Add another student? (y/n): ') == 'n':
                break
        for x in self.houses:
            print ''
            x.print_students()

    def display_art(self):
        lines = []
        with open('sorting_hat_ascii.txt', 'r') as f:
            lines = [x.strip('\n') for x in f.readlines()]
        for x in lines:
            print x

    def assign_student_with_laptop(self, name):
        while True:
            house = random.choice([self.slytherin, self.ravenclaw])
            # print house

            if house.slots_with_laptop != 0 and house.slots_taken < house.max_slots:
                house.add_student_with_laptop(name)
                return

    def assign_student_without_laptop(self, name):
        while True:
            house = random.choice([self.ravenclaw, self.gryffindor, self.hufflepuff])
            # print house

            if house.slots_without_laptop != 0 and house.slots_taken < house.max_slots:
                house.add_student_without_laptop(name)
                return
