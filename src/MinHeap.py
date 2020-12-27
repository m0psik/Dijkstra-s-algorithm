class Elem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MinHeap:
    def __init__(self):
        self.data = list()
        self.index = dict()

    def __contains__(self, item):
        return item in self.index.keys()

    def __len__(self):
        return len(self.data)

    def sift_up(self, index):
        while index > 0 and self.data[index].value < self.data[(index - 1) // 2].value:
            self.data[index], self.data[(index - 1) // 2] = self.data[(index - 1) // 2], self.data[index]
            self.index[self.data[index].key] = index
            self.index[self.data[(index - 1) // 2].key] = (index - 1) // 2
            index = (index - 1) // 2

    def sift_down(self, index):
        while True:
            bufIndex = index
            if 2 * index + 1 < len(self.data) and self.data[2 * index + 1].value < self.data[bufIndex].value:
                bufIndex = 2 * index + 1
            if 2 * index + 2 < len(self.data) and self.data[2 * index + 2].value < self.data[bufIndex].value:
                bufIndex = 2 * index + 2
            if bufIndex == index:
                break
            self.data[index], self.data[bufIndex] = self.data[bufIndex], self.data[index]
            self.index[self.data[index].key] = index
            self.index[self.data[bufIndex].key] = bufIndex
            index = bufIndex

    def insert(self, key, value):
        newElem = Elem(key, value)
        if key in self.index.keys():
            return
        self.data.append(newElem)
        self.index[key] = len(self.data) - 1
        self.sift_up(self.index[key])

    def pop_min(self):
        if len(self.data) == 0:
            return
        result = self.delete()
        return result.key, result.value

    def set(self, key, value):
        if key not in self.index.keys():
            return
        else:
            index = self.index[key]
            self.data[index].value = value
            if index < len(self.data):
                self.sift_up(index)
            self.sift_down(index)

    def delete(self, key=None):
        if key is None:
            index = 0
        elif key in self.index.keys():
            index = self.index[key]
        else:
            return
        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        self.index[self.data[index].key] = index
        result = self.data.pop()
        self.index.pop(result.key)
        if index < len(self.data):
            self.sift_up(index)
        self.sift_down(index)
        return result

    def get_value(self, key):
        return self.data[self.index[key]].value

    def get_min(self):
        if len(self.data) == 0:
            return
        return self.data[0].key, self.data[0].value
