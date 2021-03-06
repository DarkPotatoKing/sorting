from __future__ import division
from house import House
import math
import random
import os

class SortingHat:

    def start(self):
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
        min_students_per_house = int(self.num_students / 4)

        # purely laptop class
        self.slytherin = House('Slytherin', min_students_per_house, max_students_per_house, 0, -1)

        # 10 slots without laptop, the rest with laptops
        self.ravenclaw = House('Ravenclaw', min_students_per_house, max_students_per_house, 10, -1)

        # normal labs
        self.hufflepuff = House('Hufflepuff', min_students_per_house, max_students_per_house)
        self.gryffindor = House('Gryffindor', min_students_per_house, max_students_per_house)

        self.houses = [self.slytherin, self.ravenclaw, self.hufflepuff, self.gryffindor]

        # for x in self.houses:
        #     print x

    def sort_students(self):
        while True:
            os.system('clear')
            self.display_art('bootcamp_ascii.txt')
            self.display_art('sorting_hat_ascii.txt')

            name = raw_input('Enter your name:\t\t')
            has_laptop = raw_input('Can you bring a laptop (y/n):\t').lower()
            has_laptop = has_laptop == 'y' or has_laptop == 'yes'
            # print has_laptop

            if has_laptop:
                self.assign_student_with_laptop(name)
            else:
                self.assign_student_without_laptop(name)

            if raw_input('Add another student? (y/n): ') == 'n':
                break
        self.print_students_to_file()
        self.print_students()
        self.save()

    def save(self):
        for x in self.houses:
            x.save()

    def load(self):
        self.slytherin = House()
        # print self.slytherin
        self.gryffindor = House()
        self.ravenclaw = House()
        self.hufflepuff = House()

        self.slytherin.load('Slytherin.sv')
        # print self.Slytherin
        self.gryffindor.load('Gryffindor.sv')
        self.ravenclaw.load('Ravenclaw.sv')
        self.hufflepuff.load('Hufflepuff.sv')

        self.houses = [self.slytherin, self.gryffindor, self.hufflepuff, self.ravenclaw]


    def print_students_to_file(self):
        for x in self.houses:
            print ''
            # x.print_students()
            x.print_students_to_file()

    def print_students(self):
        for x in self.houses:
             x.print_students()

    def display_art(self, filename):
        lines = []
        with open(filename, 'r') as f:
            lines = [x.strip('\n') for x in f.readlines()]
        for x in lines:
            print x

    def assign_student_with_laptop(self, name):
        while True:
            choices = [self.slytherin, self.ravenclaw]
            house = random.choice(choices)
            # print house

            if house.slots_with_laptop != 0 and house.slots_taken < house.min_slots:
                house.add_student_with_laptop(name)
                return
            elif house.min_slots <= house.slots_taken < house.max_slots:
                unfilled_houses = 0
                for x in choices:
                    if x.slots_taken < x.min_slots:
                        unfilled_houses += 1
                if unfilled_houses == 0:
                    house.add_student_with_laptop(name)
                    return

    def assign_student_without_laptop(self, name):
        while True:
            choices = [self.ravenclaw, self.gryffindor, self.hufflepuff]
            house = random.choice(choices)
            # print house

            if house.slots_without_laptop != 0 and house.slots_taken < house.min_slots:
                house.add_student_without_laptop(name)
                return
            elif house.min_slots <= house.slots_taken < house.max_slots:
                unfilled_houses = 0
                for x in choices:
                    if x.slots_taken < x.min_slots:
                        unfilled_houses += 1
                if unfilled_houses == 0:
                    house.add_student_without_laptop(name)
                    return