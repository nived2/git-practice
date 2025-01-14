import unittest
from system_info import get_memory_info, get_system_info

class TestSystemInfo(unittest.TestCase):
    def test_memory_info(self):
        """Test if memory info returns the correct structure"""
        memory_info = get_memory_info()
        
        # Check if all required keys are present
        required_keys = {'total_gb', 'available_gb', 'used_gb', 'percentage'}
        self.assertEqual(set(memory_info.keys()), required_keys)
        
        # Check if values are of correct type and in valid ranges
        self.assertIsInstance(memory_info['total_gb'], float)
        self.assertIsInstance(memory_info['available_gb'], float)
        self.assertIsInstance(memory_info['used_gb'], float)
        self.assertIsInstance(memory_info['percentage'], float)
        
        # Check if values make sense
        self.assertGreater(memory_info['total_gb'], 0)
        self.assertLessEqual(memory_info['available_gb'], memory_info['total_gb'])
        self.assertGreaterEqual(memory_info['percentage'], 0)
        self.assertLessEqual(memory_info['percentage'], 100)

    def test_system_info(self):
        """Test if system info returns the correct structure"""
        system_info = get_system_info()
        
        # Check if all required keys are present
        required_keys = {'system', 'platform', 'processor', 'cpu_usage', 'memory', 'timestamp'}
        self.assertEqual(set(system_info.keys()), required_keys)
        
        # Check if values are of correct type
        self.assertIsInstance(system_info['system'], str)
        self.assertIsInstance(system_info['platform'], str)
        self.assertIsInstance(system_info['processor'], str)
        self.assertIsInstance(system_info['cpu_usage'], float)
        self.assertIsInstance(system_info['memory'], dict)
        self.assertIsInstance(system_info['timestamp'], str)

if __name__ == '__main__':
    unittest.main()
