import random
from time import thread_time


class PyList:
    def __init__(self, contents=[], size=10):
        # The contents allows the programmer to construct a list with
        # the initial contents of this value. The initial_size
        # lets the programmer pick a size for the internal size of the 
        # list. This is useful if the programmer knows he/she is going 
        # to add a specific number of items right away to the list.
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        self.appendCount = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        # raise NotImplementedError
        # gets the item from the list at the given index
        if index >= self.numItems:
            raise IndexError("PyList index out of range")
        else:
            return self.items[index]

    def __setitem__(self, index, val):
        # raise NotImplementedError

        if index >= self.numItems:
            raise IndexError("PyList index out of range")
        else:
            self.items[index] = val

    def insert(self, i, e):
        # raise NotImplementedError
        # Sticks element to a specific index
        if self.numItems == self.size:
            self.__makeroom()

        if i < self.numItems:
            for j in range(self.numItems, i - 1, -1):
                self.items[j + 1] = self.items[j]
            self.items[i] = e
            self.numItems += 1



        else:
            self.append(e)

    def __add__(self, other):
        # raise NotImplementedError
        # stick one list to the end of another
        result = PyList()

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(other.numItems):
            result.append(other.items[i])

        return result

    def __contains__(self, item):
        # is the given item in the list
        for i in range(self.numItems):
            if self.items[i] == item:
                return True

        return False

    def __delitem__(self, index):
        for i in range(index, self.numItems - 1):
            self.items[i] = self.items[i + 1]
        self.numItems -= 1  # same as writing self.numItems = self.numItems - 1

    def __eq__(self, other):
        # If two things are equal
        if type(other) != type(self):
            return False

        if self.numItems != other.numItems:
            return False

        for i in range(self.numItems):
            if self.items[i] == other.items[i]:
                pass
            else:
                return False

        return True

    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

    def __len__(self):
        return self.numItems

    # This method is hidden since it starts with two underscores. 
    # It is only available to the class to use. 
    def __makeroom(self):
        # increase list size by 1/4 to make more room.
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.size = newlen

    def append(self, item):
        # Append to the end of a list
        if self.numItems == self.size:
            self.__makeroom()
        self.items[self.numItems] = item
        self.numItems += 1
        self.appendCount += 1

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "]"
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s

    def resetAppendCount(self):
        self.appendCount = 0

    def appendCount(self):
        return self.appendCount

    def swap(self, index1, index2):
        if index1 >= self.numItems or index2 >= self.numItems:
            raise IndexError
        elif index1 == index2:
            pass
        else:
            item1 = self.items[index1]
            item2 = self.items[index2]
            self.items[index1] = item2
            self.items[index2] = item1

    def is_sorted(self):
        for i in range(self.numItems - 1):
            if self[i] > self[i + 1]:
                return False
        return True

    def sort(self):
        pass

    def bubble_sort(self):
        while not self.is_sorted():
            for i in range(self.numItems - 1):
                if self.items[i] > self.items[i + 1]:
                    self.swap(i, i + 1)


def almost_sorted(lstlen=10, swap=2):
    nums = list(range(lstlen))
    lst = PyList(nums)
    for i in range(swap):
        lst.swap(random.randint(0, lstlen - 1), random.randint(0, lstlen - 1))
    return lst


def sort_runtime(lst):
    runtime = thread_time()
    lst.bubble_sort()
    runtime = thread_time() - runtime
    return runtime


def main():
    lst = PyList()

    for i in range(100):
        lst.append(i)

    lst2 = PyList(lst)

    print(lst)
    print(lst2)

    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    lst3 = lst + lst2

    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")

    del lst[1]

    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")

    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")

    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")

    del lst2[2]

    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")

    lst4 = PyList(lst)
    lst.insert(0, 100)
    lst4 = PyList([100]) + lst4

    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")

    lst.insert(1000, 333)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")

    print(lst)
    print(lst4)

    lst5 = PyList([0, 1, 2, 3, 4])
    if lst5.is_sorted():
        print("Test 11 passed")
    else:
        print("Test 11 failed")

    lst5 = PyList(range(10))
    lst5.swap(0, 1)
    lst6 = PyList([1, 0, 2, 3, 4, 5, 6, 7, 8, 9])
    if lst5 == lst6:
        print("Test 12 passed")
    else:
        print("Test 12 failed")

    nums = list(range(20))
    random.shuffle(nums)
    lst7 = PyList(nums)
    lst8 = PyList(range(20))
    lst7.bubble_sort()
    if lst7 == lst8:
        print("Test 13 passed")
    else:
        print("Test 13 failed")

    lst9 = almost_sorted(20, 2)
    print(lst9)

    with open("almostSortedData.csv", "w") as f:
        for i in range(1000):
            lst9 = almost_sorted(i + 3, 2)
            sortTime = sort_runtime(lst9)
            f.write(f"{sortTime},\n")
    with open("randomData.csv", "w") as f:
        for i in range(1000):
            tosort = list(range(i + 3))
            random.shuffle(tosort)
            lst9 = PyList(tosort)
            sortTime = sort_runtime(lst9)
            f.write(f"{sortTime},\n")
    with open("backwardsData.csv", "w") as f:
        for i in range(1000):
            tosort = list(range(i + 3, 0, -1))
            lst9 = PyList(tosort)
            sortTime = sort_runtime(lst9)
            f.write(f"{sortTime},\n")


if __name__ == "__main__":
    main()
