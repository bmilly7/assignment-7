class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  # Fixed typo

    def __repr__(self):
        return f"Patient({self.name}, urgency={self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []  # list of Patient objects

    def heapify_up(self, index):
        """Move a node up until the heap property is restored."""
        while index > 0:
            parent_index = (index - 1) // 2
            current_patient = self.data[index]
            parent_patient = self.data[parent_index]

            # Compare urgency (lower number = more urgent)
            if current_patient.urgency < parent_patient.urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        """Move a node down until the heap property is restored."""
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            # Compare left child
            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            # Compare right child
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            # If the smallest is not the current node, swap
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    def insert(self, patient):
        """Add a new patient and reorder the heap."""
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def remove_min(self):
        """Remove and return the most urgent patient."""
        if not self.data:
            return None

        # Swap first and last
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        most_urgent = self.data.pop()
        self.heapify_down(0)
        return most_urgent

    def peek(self):
        """Return the most urgent patient without removing."""
        return self.data[0] if self.data else None

    def print_heap(self):
        """Print each patient and their urgency."""
        if not self.data:
            print("Heap is empty.")
        else:
            for p in self.data:
                print(f"{p.name} (Urgency: {p.urgency})")




# Create some patients
p1 = Patient("Alice", 4)
p2 = Patient("Bob", 1)
p3 = Patient("Charlie", 6)
p4 = Patient("Dana", 2)

# Create heap and add patients
heap = MinHeap()
heap.insert(p1)
heap.insert(p2)
heap.insert(p3)
heap.insert(p4)

print("All patients in heap:")
heap.print_heap()

print("\nMost urgent patient:", heap.peek())

print("\nTreating patients in order of urgency:")
while heap.peek():
    patient = heap.remove_min()
    print(f"Treating {patient.name} (Urgency: {patient.urgency})")







'''



A tree structure is appropriate for the doctor structure because it allows information, such as reports or patient data, to be organized hierarchically. 
Each doctor node can connect to multiple reports or subrecords, making it efficient to search, insert, or manage data in a structured and logical way. 
Software engineers use different traversal methods depending on the task. Preorder traversal is useful when copying or exporting an entire tree structure because it visits each node before its children. 
Inorder traversal is typically used when the data needs to be retrieved in a sorted order, such as from a binary search tree. Postorder traversal is helpful when deleting nodes or freeing memory, since it processes child nodes before the parent. 
Heaps help simulate real-time systems like emergency intake by prioritizing tasks or patients based on urgency. In such systems, the heap ensures that the most critical or urgent case (the smallest or highest-priority value) is always handled first, 
allowing for efficient and fair resource allocation in time-sensitive environments.





'''

