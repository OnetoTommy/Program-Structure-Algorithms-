import heapq

class PriorityQueue:
    def __init__(self):
        """Initialize a priority queue using a min-heap."""
        self.heap = []
        self.entry_finder = {}  # Map of item to its heap entry
        self.REMOVED = "<removed>"  # Placeholder for removed elements
        self.counter = 0  # Unique sequence count to avoid comparison issues

    def push(self, item, priority):
        """Add a new item or update the priority of an existing item."""
        if item in self.entry_finder:
            self.remove(item)  # Remove the existing entry before adding a new one
        entry = [priority, self.counter, item]  # Tuple format: (priority, counter, item)
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)
        self.counter += 1  # Ensure uniqueness in case of ties in priority

    def pop(self):
        """Remove and return the lowest-priority item."""
        while self.heap:
            priority, _, item = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.entry_finder[item]  # Remove from dictionary
                return item
        raise KeyError("Pop from an empty priority queue")

    def remove(self, item):
        """Mark an existing item as removed."""
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED  # Mark as removed

    def decrease_key(self, item, priority):
        """Decrease the priority of an item (or insert it if not present)."""
        self.push(item, priority)

    def is_empty(self):
        """Check if the priority queue is empty."""
        return not self.entry_finder

# Example Usage
pq = PriorityQueue()
pq.push("A", 5)
pq.push("B", 2)
pq.push("C", 8)
pq.decrease_key("A", 1)  # Lowering priority of "A"
print(pq.pop())  # Should return "A" as it now has the lowest priority
print(pq.pop())  # Should return "B"
