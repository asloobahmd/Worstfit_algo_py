import unittest
from memory_manager import MemoryManager

class TestMemoryManager(unittest.TestCase):
    def test_worst_fit_allocate(self):
        memory_blocks = [100, 500, 200, 300, 600]
        processes = [212, 417, 112, 426]
        manager = MemoryManager(memory_blocks)
        allocation = manager.worst_fit_allocate(processes)

        self.assertEqual(allocation, {0: 600, 1: 500, 2: 300, 3: None})

if __name__ == "__main__":
    unittest.main()