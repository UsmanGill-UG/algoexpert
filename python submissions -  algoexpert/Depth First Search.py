class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = [self]
        while len(stack) > 0:
            curr = stack.pop()
            array.append(curr.name)
            for i in reversed(range(len(curr.children))):
                stack.append(curr.children[i])
        return array
    
    def depthFirstSearch_R(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch_R(array)
        return array

