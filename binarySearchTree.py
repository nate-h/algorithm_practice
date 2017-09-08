# #############################################################################
# Create binary search tree
# #############################################################################


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, list):
        self.root = None
        self.size = 0

        # add items in lsit
        for value in list:
            self.add(value)

    # add value to tree
    def add(self, value):

        bstNode = BSTNode(value)

        if self.root is None:
            self.root = bstNode
            self.size += 1
            return

        currentNode = self.root

        # repeat until current node is null and add there
        while currentNode is not None:

            # if new node is greater current node -> currentNode
            if bstNode.value > currentNode.value:
                if currentNode.right is not None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = bstNode
                    break

            # if new node is less than or equals to current node
            elif bstNode.value <= currentNode.value:
                if currentNode.left is not None:
                    currentNode = currentNode.left
                else:
                    currentNode.left = bstNode
                    break

        bstNode.parent = currentNode
        self.size += 1
        return

    # find value and remove
    def remove(self, value):
        pass

    # print out values in order using in-order tree traversal
    def __str__(self):
        logStr = "Printing out tree\n"
        logStr += "Size: {}\n".format(self.size)
        preString = ""
        self.inOrder(self.root, preString)
        logStr += preString
        return logStr

    def inOrder(self, currentNode, logStr):

        # 1. Check if node is empty
        if currentNode is None:
            return

        # 2. traverse left subtree calling in order function
        self.inOrder(currentNode.left, logStr)

        # 3. print node
        logStr += "{} ".format(currentNode.value)

        # 4. traverse right subtree
        self.inOrder(currentNode.right, logStr)
        return


if __name__ == "__main__":
    bst = BinarySearchTree([6, 3, 4, 7, 8, 6, 4, 9, 1, 0])
    print(bst)
