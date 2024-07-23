import time


class SortingAlgorithm:
    def __init__(self, array, draw_array, speed):
        self.array = array
        self.draw_array = draw_array
        self.speed = speed
        self.paused = False

    def sort(self):
        raise NotImplementedError

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def is_paused(self):
        return self.paused

    def check_pause(self):
        while self.paused:
            time.sleep(0.1)


class BubbleSort(SortingAlgorithm):
    def sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.paused:
                    self.check_pause()
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array(self.array, [j, j + 1])
                    time.sleep(self.speed)
        self.draw_array(self.array, [])


class SelectionSort(SortingAlgorithm):
    def sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.paused:
                    self.check_pause()
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array(self.array, [i, min_idx])
            time.sleep(self.speed)
        self.draw_array(self.array, [])


class InsertionSort(SortingAlgorithm):
    def sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                if self.paused:
                    self.check_pause()
                self.array[j + 1] = self.array[j]
                j -= 1
                self.draw_array(self.array, [j + 1, i])
                time.sleep(self.speed)
            self.array[j + 1] = key
            self.draw_array(self.array, [j + 1])
        self.draw_array(self.array, [])


class MergeSort(SortingAlgorithm):
    def sort(self):
        self._merge_sort(0, len(self.array) - 1)
        self.draw_array(self.array, [])

    def _merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(left, mid)
            self._merge_sort(mid + 1, right)
            self._merge(left, mid, right)

    def _merge(self, left, mid, right):
        L = self.array[left : mid + 1]
        R = self.array[mid + 1 : right + 1]

        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if self.paused:
                self.check_pause()
            if L[i] <= R[j]:
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            k += 1
            self.draw_array(self.array, [k])
            time.sleep(self.speed)

        while i < len(L):
            self.array[k] = L[i]
            i += 1
            k += 1
            self.draw_array(self.array, [k])
            time.sleep(self.speed)

        while j < len(R):
            self.array[k] = R[j]
            j += 1
            k += 1
            self.draw_array(self.array, [k])
            time.sleep(self.speed)


class QuickSort(SortingAlgorithm):
    def sort(self):
        self._quick_sort(0, len(self.array) - 1)
        self.draw_array(self.array, [])

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        i = low - 1
        pivot = self.array[high]
        for j in range(low, high):
            if self.paused:
                self.check_pause()
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.draw_array(self.array, [i, j])
                time.sleep(self.speed)
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.draw_array(self.array, [i + 1, high])
        time.sleep(self.speed)
        return i + 1


class HeapSort(SortingAlgorithm):
    def sort(self):
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.draw_array(self.array, [i, 0])
            time.sleep(self.speed)
            self._heapify(i, 0)
        self.draw_array(self.array, [])

    def _heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.array[l] > self.array[largest]:
            largest = l

        if r < n and self.array[r] > self.array[largest]:
            largest = r

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.draw_array(self.array, [i, largest])
            time.sleep(self.speed)
            self._heapify(n, largest)
