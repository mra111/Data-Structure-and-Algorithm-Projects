import unittest
import sys
import functools

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)
      
    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)
    
    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)
    return wrapper

def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))
    return wrapper

class MainEmu():
    def __init__(self):
        self.items = dict()

    def start_program(self):
        for line in sys.stdin:
            line = Utils.delete_end_char(line)
            action, line = Utils.parse_line(line)
            actionPointer = Utils.get_attribute_pointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = Utils.parse_line(line)
        itemName, line = Utils.parse_line(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = Utils.parse_line(line, '.')
        funcName, line = Utils.parse_line(line, '(')
        argsLine, line = Utils.parse_line(line, ')')
        args = Utils.get_args(argsLine)
        attribute = Utils.get_attribute_pointer(self.items[itemName],
                                                   funcName)

        Utils.run_function(attribute, args)

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class MinHeap:
    def __init__(self):
        self.heap = []
    
    class Node:
        pass
        
    def bubble_up(self, index):
        if (type (index) != int):
            raise Exception ("invalid index")

        if (len (self.heap) - 1 < index or index < 0):
            raise Exception ("out of range index")
        
        if (index > 0 and self.heap[index] < self.heap[int ((index - 1) / 2)]):
            self.heap[index],self.heap[int ((index - 1) / 2)] = self.heap[int ((index - 1) / 2)],self.heap[index]
            self.bubble_up (int ((index - 1) / 2))
            
    def bubble_down(self, index):
        if (type (index) != int):
            raise Exception ("invalid index")

        if (len (self.heap) - 1 < index or index < 0):
            raise Exception ("out of range index")
        
        if (len (self.heap) <= 1):
            return
        
        if (index <= int (len (self.heap) / 2) - 1):
            if (2 * index + 2 <= len (self.heap) - 1):

                if (self.heap[2 * index + 1] < self.heap[2 * index + 2] and self.heap[index] > self.heap[2 * index + 1]):
                    self.heap[index],self.heap[2 * index + 1] = self.heap[2 * index + 1],self.heap[index]
                    self.bubble_down (2 * index + 1)
                    
                elif (self.heap[index] > self.heap[2 * index + 2]):
                    self.heap[index],self.heap[2 * index + 2] = self.heap[2 * index + 2],self.heap[index]
                    self.bubble_down (2 * index + 2)

            elif (self.heap[index] > self.heap[2 * index + 1]):
                self.heap[index],self.heap[2 * index + 1] = self.heap[2 * index + 1],self.heap[index]
                self.bubble_down (2 * index + 1)
    
    def heap_push(self, value):
        self.heap.append (value)

        self.bubble_up (len (self.heap) - 1)
        
    def heap_pop(self):
        if (len (self.heap) == 0):
            raise Exception ("empty")
        
        root = self.heap[0]

        self.heap[0],self.heap[len (self.heap) - 1] = self.heap[len (self.heap) - 1],self.heap[0]
        self.heap.pop ()

        if (len (self.heap) > 0):
            self.bubble_down (0)

        return root
    
    def find_min_child(self, index):
        if (type (index) != int):
            raise Exception ("invalid index")

        if (index < 0 or index > len (self.heap)):
            raise Exception ("out of range index")
        
        if (len (self.heap) == 0):
            raise Exception ("empty")
        
        if (2 * index + 2 >= len (self.heap)):
            return (2 * index + 1)
        
        if (self.heap[2 * index + 1] < self.heap[2 * index + 2]):
            return (2 * index + 1)
        else:
            return (2 * index + 2)
            
    def heapify(self, *args):
        self.heap = list (args)

        for i in range ((int (len (self.heap) / 2)) - 1, -1, -1):
            self.bubble_down (i)

class HuffmanTree:
    def __init__(self):
        self.letters = []
        self.counts = []
        self.tree = []
        self.cost = 0

    @fix_str_arg    
    def set_letters(self,*args):
        self.letters = args

    @fix_str_arg    
    def set_repetitions(self,*args):
        self.tree = list (args)

    class Node:
        pass

    def build_huffman_tree(self):
        while (len (self.tree) > 1):
            n1 = self.tree.pop (self.tree.index (min (self.tree)))
            n2 = self.tree.pop (self.tree.index (min (self.tree)))

            self.tree.append (n1 + n2)

            self.cost = self.cost + n1 + n2

    def get_huffman_code_cost(self):
        return self.cost

    @fix_str_arg
    def text_encoding(self, text):
        self.tree = []
        self.letters = []

        for i in range (len (text)):
            if (text[i] in self.letters):
                index = self.letters.index (text[i])
                self.tree[index] = self.tree[index] + 1
            else:
                self.letters.append (text[i])
                self.tree.append (1)
        
        self.build_huffman_tree ()

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class RedBlackTree():
    def __init__(self):
        self.root = None
        
    class Node:
        def __init__ (self, value):
            self.value = value
            self.color = "R"
            self.parent = None
            self.right = None
            self.left = None

    def fix_insert(self, node):
        if (node == self.root):
            node.color = "B"
            return

        if (node.parent.color == "B"):
            return
        
        if (node.parent.parent.right == None or node.parent.parent.left == None or node.parent.parent.right.color == "B" or node.parent.parent.left.color == "B"):
            if (node.parent.parent.left == node.parent):
                if (node == node.parent.right):
                    self.left_rotate (node.parent)
                    self.fix_insert (node.left)
                else:
                    self.right_rotate (node.parent.parent)
                    node.parent.color = "B"
                    node.parent.right.color = "R"
            else:
                if (node == node.parent.left):
                    self.right_rotate (node.parent)
                    self.fix_insert (node.right)
                else:
                    self.left_rotate (node.parent.parent)
                    node.parent.color = "B"
                    node.parent.left.color = "R"
            
        elif (node.parent.parent.right.color == "R" and node.parent.parent.left.color == "R"):
            node.parent.parent.right.color = "B"
            node.parent.parent.left.color = "B"
            node.parent.parent.color = "R"
            self.fix_insert (node.parent.parent)
            
    def find_node (self, value, node):
        if (value == node.value):
            return node
        
        if (value > node.value):
            return (self.find_node (value, node.right))
        else:
            return (self.find_node (value, node.left))

    def find_node_color(self, value):
        node = self.find_node (value, self.root)

        if (node.color == "B"):
            return ("BLACK")
        else:
            return ("RED")

    def left_rotate(self, node):
        child_node = node.right
        child_node.parent = node.parent

        if (node == self.root):
            self.root = child_node

        if (child_node.parent != None and child_node.parent.right == node):
            child_node.parent.right = child_node
        elif (child_node.parent != None):
            child_node.parent.left = child_node
        
        node.right = child_node.left

        if (node.right != None):
            node.right.parent = node
        
        child_node.left = node
        node.parent = child_node

    def right_rotate(self, node):
        child_node = node.left
        child_node.parent = node.parent

        if (node == self.root):
            self.root = child_node

        if (child_node.parent != None and child_node.parent.right == node):
            child_node.parent.right = child_node
        elif (child_node.parent != None):
            child_node.parent.left = child_node
        
        node.left = child_node.right

        if (node.left != None):
            node.left.parent = node
        
        child_node.right = node
        node.parent = child_node

    def find_value (self, value, node):
        if (value >= node.value):
            if (node.right == None):
                return node
            
            return (self.find_value (value, node.right))
        else:
            if (node.left == None):
                return node
            
            return (self.find_value (value, node.left))
        
    def insert(self, value):
        node = self.Node (value)

        if (self.root == None):
            node.color = "B"
            self.root = node
            return
        
        parent_node = self.find_value (value, self.root)

        if (value >= parent_node.value):
            parent_node.right = node
            node.parent = parent_node
        else:
            parent_node.left = node
            node.parent = parent_node

        self.fix_insert (node)

classDict = { "min_heap": MinHeap, "red_black_tree": RedBlackTree, "huffman_tree": HuffmanTree}
    
if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()