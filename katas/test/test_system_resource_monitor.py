import unittest
from katas.system_resource_monitor import get_cpu_usage, get_memory_usage, get_disk_usage
from unittest.mock import patch, MagicMock



class TestSystemResourceMonitor(unittest.TestCase):
    @patch('katas.system_resource_monitor.psutil.cpu_count')
    @patch('katas.system_resource_monitor.psutil.cpu_percent')
    def test_get_cpu_usage(self, mock_cpu_percent, mock_cpu_count):
        mock_cpu_count.return_value = 4
        mock_cpu_percent.side_effect = [20.0, [20.0, 25.0, 15.0, 30.0]]
        
        cpu_info = get_cpu_usage()
        
        self.assertEqual(cpu_info['core_count'], 4)
        self.assertEqual(cpu_info['usage_percent'], 20.0)
        self.assertEqual(cpu_info['per_core_usage'], [20.0, 25.0, 15.0, 30.0])
   


    @patch('katas.system_resource_monitor.psutil.virtual_memory')
    def test_get_memory_usage(self, mock_virtual_memory):
        mock_mem = MagicMock()
        mock_mem.total = 8 * (1024 ** 3)  # 8 GB
        mock_mem.available = 3 * (1024 ** 3)  # 3 GB
        mock_mem.used = 5 * (1024 ** 3)  # 5 GB
        mock_virtual_memory.return_value = mock_mem
        
        mem_info = get_memory_usage()
        
        self.assertEqual(mem_info['total_gb'], 8.00)
        self.assertEqual(mem_info['available_gb'], 3.00)
        self.assertEqual(mem_info['used_gb'], 5.00)

    @patch('katas.system_resource_monitor.psutil.disk_usage')
    def test_get_disk_usage(self, mock_disk_usage):
        mock_disk = MagicMock()
        mock_disk.total = 500 * (1024 ** 3)  # 500 GB
        mock_disk.used = 200 * (1024 ** 3)   # 200 GB
        mock_disk.free = 300 * (1024 ** 3)   # 300 GB
        mock_disk.percent = 40.0
        mock_disk_usage.return_value = mock_disk
        
        disk_info = get_disk_usage("/")
        
        self.assertEqual(disk_info['total_gb'], 500.00)
        self.assertEqual(disk_info['used_gb'], 200.00)
        self.assertEqual(disk_info['free_gb'], 300.00)
        self.assertEqual(disk_info['usage_percent'], 40.0)

if __name__ == '__main__':
    unittest.main()