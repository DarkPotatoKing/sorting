class SortingHat:
    num_students = 0
    slytherin = None
    gryffindor  = None
    ravenclaw = None
    hufflepuff = None

    def __init__(self):
        self.load_config()
        print self.num_students

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
