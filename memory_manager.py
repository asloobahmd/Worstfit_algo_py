class MemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks  # List of memory block sizes
        self.allocation = {}  # Dictionary to store process allocations

    def worst_fit_allocate(self, processes):
        for process_id, process_size in enumerate(processes):
            # Sort blocks in descending order of size
            self.memory_blocks.sort(reverse=True)
            allocated = False

            for i, block_size in enumerate(self.memory_blocks):
                if block_size >= process_size:
                    self.allocation[process_id] = block_size
                    self.memory_blocks[i] -= process_size
                    if self.memory_blocks[i] == 0:
                        # Remove the block if it's fully used
                        self.memory_blocks.pop(i)
                    allocated = True
                    break

            if not allocated:
                self.allocation[process_id] = None  # Process not allocated

        return self.allocation