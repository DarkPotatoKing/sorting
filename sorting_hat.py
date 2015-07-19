from __future__ import division
from house import House
import math

class SortingHat:
    num_students = 0
    slytherin = House()
    gryffindor  = House()
    ravenclaw = House()
    hufflepuff = House()
    

    def __init__(self):
        self.load_config()
        self.assign_house_slots()

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
        
        for x in self.houses:
            print x
