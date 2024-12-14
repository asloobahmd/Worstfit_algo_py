from memory_manager import MemoryManager

def main():
    print("Enter memory block sizes (comma-separated): ")
    memory_blocks = list(map(int, input().split(',')))

    print("Enter process sizes (comma-separated): ")
    processes = list(map(int, input().split(',')))

    manager = MemoryManager(memory_blocks)
    allocation = manager.worst_fit_allocate(processes)

    print("\nAllocation Results:")
    for process_id, block in allocation.items():
        if block is not None:
            print(f"Process {process_id} -> Block of size {block}")
        else:
            print(f"Process {process_id} -> Not Allocated")

if __name__ == "__main__":
    main()