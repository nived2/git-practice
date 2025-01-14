import unittest
from system_info import get_memory_info, get_system_info, get_disk_info, get_network_info

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

    def test_disk_info(self):
        """Test if disk info returns the correct structure"""
        disk_info = get_disk_info()
        
        # Check if we got any disk information
        self.assertGreater(len(disk_info), 0)
        
        # Check structure for each mount point
        for mount_point, info in disk_info.items():
            self.assertIsInstance(mount_point, str)
            required_keys = {'total_gb', 'used_gb', 'free_gb', 'percentage', 'fstype'}
            self.assertEqual(set(info.keys()), required_keys)
            
            # Check value types and ranges
            self.assertIsInstance(info['total_gb'], float)
            self.assertIsInstance(info['used_gb'], float)
            self.assertIsInstance(info['free_gb'], float)
            self.assertIsInstance(info['percentage'], float)
            self.assertIsInstance(info['fstype'], str)
            
            # Check if values make sense
            self.assertGreater(info['total_gb'], 0)
            self.assertGreaterEqual(info['percentage'], 0)
            self.assertLessEqual(info['percentage'], 100)

    def test_network_info(self):
        """Test if network info returns the correct structure"""
        network_info = get_network_info()
        
        # Check if we got any network information
        self.assertGreater(len(network_info), 0)
        
        # Check structure for each interface
        for interface, info in network_info.items():
            self.assertIsInstance(interface, str)
            required_keys = {
                'bytes_sent_mb', 'bytes_recv_mb', 'packets_sent',
                'packets_recv', 'errors_in', 'errors_out',
                'dropped_in', 'dropped_out'
            }
            self.assertEqual(set(info.keys()), required_keys)
            
            # Check value types
            self.assertIsInstance(info['bytes_sent_mb'], float)
            self.assertIsInstance(info['bytes_recv_mb'], float)
            self.assertIsInstance(info['packets_sent'], int)
            self.assertIsInstance(info['packets_recv'], int)
            
            # Check if values make sense
            self.assertGreaterEqual(info['bytes_sent_mb'], 0)
            self.assertGreaterEqual(info['bytes_recv_mb'], 0)
            self.assertGreaterEqual(info['packets_sent'], 0)
            self.assertGreaterEqual(info['packets_recv'], 0)

    def test_system_info(self):
        """Test if system info returns the correct structure"""
        system_info = get_system_info()
        
        # Check if all required keys are present
        required_keys = {'system', 'platform', 'processor', 'cpu_usage',
                        'memory', 'disk', 'network', 'timestamp'}
        self.assertEqual(set(system_info.keys()), required_keys)
        
        # Check if values are of correct type
        self.assertIsInstance(system_info['system'], str)
        self.assertIsInstance(system_info['platform'], str)
        self.assertIsInstance(system_info['processor'], str)
        self.assertIsInstance(system_info['cpu_usage'], float)
        self.assertIsInstance(system_info['memory'], dict)
        self.assertIsInstance(system_info['disk'], dict)
        self.assertIsInstance(system_info['network'], dict)
        self.assertIsInstance(system_info['timestamp'], str)

if __name__ == '__main__':
    unittest.main()
