from katas.pinger import ping_host
import unittest
from unittest.mock import patch, MagicMock

class TestPinger(unittest.TestCase):
    @patch('katas.pinger.subprocess.run')
    def test_ping_host_success(self, mock_run):
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_process.stdout = "round-trip min/avg/max/stddev = 13.986/14.400/14.934/0.396 ms"
        mock_run.return_value = mock_process
        result = ping_host("example.com", count=3)
        self.assertEqual(result['host'], "example.com")
        self.assertAlmostEqual(result['avg_response_time_ms'], 14.400)
        self.assertTrue(result['success'])  
if __name__ == '__main--':
    unittest.main()