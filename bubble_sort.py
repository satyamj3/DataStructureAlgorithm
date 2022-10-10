from copy import deepcopy


class BubbleSort:
    def __init__(self, data_list=[]):
        self.arr = data_list
        self.len = len(data_list)

    def __str__(self):
        return ', '.join([str(elem) for elem in self.arr])

    def sort(self):
        """
        Sorting using for loop.
        """
        for i in range(self.len):
            for j in range(self.len - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    tmp = deepcopy(self.arr[j])
                    self.arr[j] = self.arr[j + 1]
                    self.arr[j + 1] = tmp

    def sort_rec(self, n):
        """
        Sorting using recursion.
        """
        if n == 1:
            return
        for j in range(n - 1):
            if self.arr[j] > self.arr[j + 1]:
                tmp = deepcopy(self.arr[j])
                self.arr[j] = self.arr[j + 1]
                self.arr[j + 1] = tmp
        self.sort_rec(n - 1)


arr = [12, 45, 0, -1, -56, 145]
bubble_sort = BubbleSort(deepcopy(arr))
print(bubble_sort)
bubble_sort.sort()
print(bubble_sort)

bubble_rec = BubbleSort(arr)
print(bubble_rec)
bubble_rec.sort_rec(bubble_rec.len)
print(bubble_rec)
