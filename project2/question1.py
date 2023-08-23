import sys

class Queue:
    def __init__(self):
        self.queue = []

    def getSize(self):
        return (len (self.queue))

    def enqueue(self, value):
        self.queue.append (value)

    def dequeue(self):
        if (len (self.queue) > 0):
            return (self.queue.pop (0))
        else:
            return False

    def isEmpty(self):
        if (len (self.queue) == 0):
            return True
        else:
            return False

    def getInOneLine(self):
        line = ""

        for i in self.queue:
            if (i == self.queue[0]):
                line = line + i
            else:
                line = line + " " + i
        
        return line


class Stack:
    def __init__(self, size=10):
        self.stack = []
        self.size = size

    def isEmpty(self):
        if (len (self.stack) == 0):
            return True
        else:
            return False

    def push(self, value):
        if (len (self.stack) < self.size):
            self.stack.append (value)
        else:
            return False

    def pop(self):
        if (len (self.stack) > 0):
            return (self.stack.pop ())
        else:
            return False

    def put(self,value_):
        if (len (self.stack) > 0):
            self.stack[len (self.stack) - 1] = value_
        else:
            return False

    def peek(self):
        if (len (self.stack) > 0):
            return self.stack[len (self.stack) - 1]
        else:
            return False

    def expand(self):
        self.size = 2 * self.size

    def getInOneLine(self):
        line = ""

        for i in self.stack:
            if (i == self.stack[0]):
                line = line + i
            else:
                line = line + " " + i
        
        return line

    def getSize(self):
        return (len (self.stack))
    
    def getCapacity(self):
        return (self.size)

class Node():
    def __init__(self, val):
        self.value = val

class LinkedList():
    def __init__(self):
        self.nodes_list = []
    
    def getList(self):
        line = ""

        for i in self.nodes_list:
            if (i == self.nodes_list[0]):
                line = line + i.value
            else:
                line = line + " " + i.value
        
        return line
    
    def insertFront(self, new_data):
        self.nodes_list.insert (0, Node (new_data))
    
    def insertEnd(self, new_data):
        self.nodes_list.append (Node (new_data))
    
    def reverse(self):
        self.nodes_list.reverse ()

classDict = { "stack": Stack, "queue": Queue, "linked_list": LinkedList}

class Utils():
    def __init__(self):
        pass

    def parseLine(self, line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def deleteEndChar(self, line):
        return line.rstrip(line[-1])

    def getAttributePointer(self, object, attribute):
        return getattr(object, attribute)

    def getArgs(self, argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def runFunction(self, attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)

class MainEmu():
    def __init__(self):
        self.utils = Utils()
        self.items = dict()

    def startProgram(self):
        for line in sys.stdin:
            line = self.utils.deleteEndChar(line)
            action, line = self.utils.parseLine(line)
            actionPointer = self.utils.getAttributePointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = self.utils.parseLine(line)
        itemName, line = self.utils.parseLine(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = self.utils.parseLine(line, '.')
        funcName, line = self.utils.parseLine(line, '(')
        argsLine, line = self.utils.parseLine(line, ')')
        args = self.utils.getArgs(argsLine)
        attribute = self.utils.getAttributePointer(self.items[itemName],
                                                   funcName)

        self.utils.runFunction(attribute, args)

if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.startProgram()