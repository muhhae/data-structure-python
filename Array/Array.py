class Array:
    def __init__(self, maxIndex=10):
        self.maxIndex = maxIndex
        self.data = [0] * maxIndex
        self.topIndex = -1

    def __len__(self):
        return self.topIndex + 1

    def size(self):
        return len(self)

    def at(self, index):
        if index > self.topIndex:
            return
        return self.data[index]

    def append(self, value):
        if self.topIndex < self.maxIndex - 1:
            self.topIndex += 1
            self.data[self.topIndex] = value
        else:
            print("Array is full")

    def insert(self, index, value):
        if index > self.topIndex:
            return
        self.topIndex += 1
        if self.topIndex > self.maxIndex:
            self.topIndex = self.maxIndex
        for i in range(self.topIndex, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value

    def delete(self, index):
        if index > self.topIndex :
            return
        for i in range(index, self.topIndex):
            self.data[i] = self.data[i + 1]
        self.data[self.topIndex] = 0
        self.topIndex -= 1

    def update(self, index, value):
        if index > self.topIndex:
            return
        self.data[index] = value

    def findOne(self, value):
        for i in range(self.topIndex + 1):
            if self.data[i] == value :
                return i

    def findOneAndDelete(self, value):
        for i in range(self.topIndex + 1):
            if self.data[i] == value:
                self.delete(i)
                return

    def findAllAndDelete(self, value):
        i = 0
        while i <= self.topIndex:
            if self.data[i] == value:
                self.delete(i)
            else:
                i += 1

    def findOneAndUpdate(self, old, new):
        for i in range(self.topIndex + 1):
            if self.data[i] == old :
                self.data[i] = new
                return

    def findAllAndUpdate(self, old, new):
        for i in range(self.topIndex + 1):
            if self.data[i] == old :
                self.data[i] = new

    def resize(self, newSize):
        temp = [0] * newSize
        for i in range(self.topIndex + 1):
            temp[i] = self.data[i]
        self.maxIndex = newSize
        self.data = temp

    def print(self):
        for i in range(self.topIndex + 1):
            print("data[" + str(i) + "]:", self.data[i])
