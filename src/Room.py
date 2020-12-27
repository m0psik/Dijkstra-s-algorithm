class Room:
    def __init__(self, name):
        self.name = name
        self.neighbors = dict()

    def get_all_neighbors(self):
        return self.neighbors.keys()

    def add_neighbor(self, room, distance):
        if room in self.get_all_neighbors():
            raise Exception("The edge '" + self.get_name() + '-' + room.get_name() + "' has already been added")
        self.neighbors[room] = distance

    def get_name(self):
        return self.name

    def get_distance(self, room):
        if room not in self.get_all_neighbors():
            raise Exception('The room is not adjacent')
        return self.neighbors[room]

    def get_all_distance(self):
        answer = dict()
        for room in self.neighbors:
            answer[room.get_name()] = self.neighbors[room]
        return answer
