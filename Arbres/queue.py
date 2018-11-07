
class Queue:

    def __init__(self):

        self.list = []



    def enqueue(self, data):

        self.list.append(data)



    def dequeue(self):

        if len(self.list) > 0:

            self.list.pop(0)



    def getFirst(self):

        return self.list[0]



    def isEmpty(self):

        return self.list == []

