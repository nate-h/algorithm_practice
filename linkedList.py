# #############################################################################
# Problem: create doubly-linked list that has push front/back
# remove front/back
# #############################################################################


# 1. Create link class
class Link:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


# 2. Create linked list class
class LinkedList:
    def __init__(self, list=None):
        self.head = None
        self.tail = None
        self.size = 0

        # now iterate over list and create links
        if list is not None:
            for i in list:
                self.push_back(i)

    def push_back(self, value):
        link = Link(value)
        if self.tail is not None:
            self.tail.next = link
            link.prev = self.tail
        else:
            self.head = link
        self.tail = link
        self.size += 1

    def push_front(self, value):
        link = Link(value)
        if self.head is not None:
            self.head.prev = link
            link.next = self.head
        else:
            self.tail = link
        self.head = link
        self.size += 1
        pass

    def pop_front(self):
        if self.size is 0:
            return
        if self.size > 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = None
            self.head = None
        self.size -= 1

    def pop_back(self):
        if self.size is 0:
            return
        if self.size > 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None
        self.size -= 1

    def __str__(self):
        str = "Printing List\n"
        str += "size: {}\n".format(self.size)
        link = self.head
        count = 0
        while link is not None:
            str += "LinkedList[{}] = {}\n".format(count, link.value)
            link = link.next
            count += 1
        return str

# test code
if __name__ == "__main__":

    # Create and print list
    print("Creating List")
    testList = LinkedList([1, 2, 3, 4, 5])
    print(testList)

    # test pop front
    print("\nAfter popping front and back:")
    testList.pop_front()
    testList.pop_back()
    print(testList)

    # Check pesky edge cases
    testList.pop_front()
    testList.pop_back()
    testList.pop_back()
    print(testList)

    # now adding data back to it
    testList.push_back(1)
    testList.push_back(2)
    testList.push_back(3)
    print(testList)
