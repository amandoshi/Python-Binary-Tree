class Node:
    def __init__(self, value):
        self._left = None
        self._value = value
        self._right = None

    def insertNode(self, value):
        self.addNode(self.createNode(value))

    def createNode(self, value):
        return Node(value)

    def addNode(self, newNode):
        if self._value:
            #add node to right
            if newNode._value > self._value:
                if self._right:
                    self._right.addNode(newNode)
                else:
                    self._right = newNode

            #add node to left
            else:
                if self._left:
                    self._left.addNode(newNode)
                else:
                    self._left = newNode
        else:
            self.redefineSelfNode(newNode)

    def deleteNode(self, value):
        if self._value:
            #delete root
            if value == self._value:
                node = self.restructureNode(self)
                self.redefineSelfNode(node)

            elif value > self._value and self._right:
                #delete right node
                if value == self._right._value:
                    self._right = self.restructureNode(self._right)
                #fall through right node
                else:
                    self._right.deleteNode(value)

            elif self._left:
                #delete left node
                if value == self._left._value:
                    self._left = self.restructureNode(self._left)
                #fall through left node
                else:
                    self._left.deleteNode(value)

    #restructureNode when delete value found
    def restructureNode(self, node):
        if node._right:
            leftNode = node._left
            node = node._right
            if leftNode:
                node.addNode(leftNode)

        elif node._left:
            node = node._left

        else:
            node = None

        return node

    #redefine root of tree
    def redefineSelfNode(self, newNode):
        if newNode:
            self._value = newNode._value
            self._right = newNode._right
            self._left = newNode._left
        else:
            self._value = None
            self._right = None
            self._left = None

    #return tree as string
    def inOrdertraversal(self):
        tree = ""
        if self._left:
            tree += self._left.inOrdertraversal()
        if self._value:
            tree += self._value
        if self._right:
            tree += self._right.inOrdertraversal()
        return tree

def main():
    #create tree
    myTree = Node("a")

    #test inesrtion + deletion
    string = "mandoshi"
    for char in string:
        myTree.insertNode(char)

    print(myTree.inOrdertraversal())

    myTree.deleteNode("m")
    myTree.deleteNode("a")
    myTree.deleteNode("a")

    myTree.insertNode('v')
    
    print(myTree.inOrdertraversal())

    myTree.insertNode('x')
    myTree.insertNode('a')
    myTree.insertNode('b')

    print(myTree.inOrdertraversal())

if __name__ == "__main__":
    main()
