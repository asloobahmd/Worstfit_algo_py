# Worstfit_algo_py

## **Overview**

The Worst Fit Memory Allocation System is a Python-based program designed to allocate memory blocks to processes using the Worst Fit algorithm. This system emphasizes modularity and testability by separating core functionality, user interaction, and testing logic. The system provides an efficient and straightforward approach to solving memory allocation problems, demonstrating clear allocation results and facilitating automated testing for correctness.

---

## **Key Components**

### **1. Main Program (`main.py`)**

The `main.py` script serves as the entry point for the application. It:

- Accepts memory block sizes and process sizes as input from the user.
- Instantiates the `MemoryManager` class to manage the allocation logic.
- Executes the `worst_fit_allocate` method to allocate processes to memory blocks.
- Displays the allocation results, including unallocated processes.

---

### **2. Memory Manager (`memory_manager.py`)**

The `MemoryManager` class encapsulates the core logic for memory allocation using the Worst Fit algorithm.

#### **Attributes:**

- `memory_blocks`: Stores the sizes of available memory blocks.
- `allocation`: Maintains the mapping of processes to their allocated blocks.

#### **Methods:**

- `__init__`: Initializes the memory manager with the provided memory blocks.
- `worst_fit_allocate`: Implements the Worst Fit algorithm to allocate processes to the largest available blocks.

---

### **3. Testing Module (`test_memory.py`)**

The `test_memory.py` module uses the `unittest` framework to validate the correctness of the allocation logic.

- Includes a test case, `test_worst_fit_allocate`, to verify the output of the `worst_fit_allocate` method with predefined inputs and expected results.
