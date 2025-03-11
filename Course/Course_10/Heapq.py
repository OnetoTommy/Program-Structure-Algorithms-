class MinHeap:
    def __init__(self):
        """Initialize an empty heap (Min-Heap)."""
        self.heap = []

    def heappush(self, item):
        """Push an item onto the heap, maintaining the heap property."""
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def heappop(self):
        """Pop the smallest item from the heap."""
        if not self.heap:
            raise IndexError("Pop from an empty heap")

        # Swap the first and last item, then remove the last (smallest)
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._sift_down(0)

        return min_item

    def heapify(self, array):
        """Transform a list into a valid heap in O(n) time."""
        self.heap = array[:]
        for i in reversed(range(len(self.heap) // 2)):  # Start from the first non-leaf node
            self._sift_down(i)

    def heapreplace(self, item):
        """Pop and return the smallest item, then push the new item onto the heap."""
        if not self.heap:
            raise IndexError("Heap is empty")
        min_item = self.heap[0]
        self.heap[0] = item
        self._sift_down(0)
        return min_item

    def _sift_up(self, index):
        """Move a node up in the heap until heap property is restored."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        """Move a node down in the heap until heap property is restored."""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        """Return the string representation of the heap."""
        return str(self.heap)


# Example Usage
heap = MinHeap()
heap.heappush(10)
heap.heappush(5)
heap.heappush(15)
heap.heappush(3)
heap.heappush(8)

print("Heap after insertions:", heap)

print("Pop:", heap.heappop())  # Should return 3 (smallest element)
print("Heap after pop:", heap)

heap.heapify([20, 1, 5, 12, 9])
print("Heap after heapify:", heap)

print("Heap replace (replace root with 6):", heap.heapreplace(6))
print("Heap after replacement:", heap)
