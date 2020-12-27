from Room import Room
from MinHeap import MinHeap
from collections import defaultdict, deque
import math


class Dungeon:
    def __init__(self):
        self.rooms = defaultdict(Room)

    def add_edge(self, start, end, distance, edge_type='d'):
        if start not in self.rooms.keys():
            room = Room(start)
            self.rooms[start] = room
        if end not in self.rooms.keys():
            room = Room(end)
            self.rooms[end] = room
        self.rooms[start].add_neighbor(self.rooms[end], distance)
        if edge_type == 'u':
            self.rooms[end].add_neighbor(self.rooms[start], distance)

    def find_way(self, start_room, end_room):
        if start_room not in self.rooms.keys() or end_room not in self.rooms.keys():
            return [None, None], 'Non-existent room'
        inf = math.inf
        dist = MinHeap()
        path = dict()
        for key in self.rooms.keys():
            dist.insert(key, inf)
        dist.set(start_room, 0)
        distance = None

        while len(dist) > 0:
            current = dist.pop_min()
            length = self.rooms[current[0]].get_all_distance()
            if current[0] == end_room:
                distance = current[1]
            for edge_to in length:
                if edge_to in dist:
                    if current[1] + length[edge_to] < dist.get_value(edge_to):
                        dist.set(edge_to, current[1] + length[edge_to])
                        path[edge_to] = current[0]
        if distance == inf:
            return [None, None], end_room + ' is unreachable from ' + start_room
        path = self.convert_path_to_string(path, start=start_room, end=end_room)
        return [path, distance], None

    @staticmethod
    def convert_path_to_string(path, start, end):
        current = end
        queue_answer = deque()
        while current != start:
            queue_answer.append(current)
            current = path[current]
        answer = start
        while len(queue_answer) != 0:
            answer += ' -> ' + queue_answer.pop()
        return answer
