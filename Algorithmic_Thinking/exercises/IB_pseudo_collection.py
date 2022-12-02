class Collection:
    def __init__(self):
        self.data = []
        self.pointer = 0

    def addItem(self, item):
        self.data.append(item)


    def getNext(self):
        item =self.data[self.pointer]
        self.pointer += 1
        return item 
    
    def resetNext(self):
        self.pointer = 0

    def hasNext(self):
        return self.pointer  < len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

test = list(range(10))

coll = Collection()

for item in test:
    coll.addItem(item)

while coll.hasNext():
    print(coll.getNext())