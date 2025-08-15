from katas.fastapi_log_parser import parse_fastapi_log
import unittest

class TestFastAPILogParser(unittest.TestCase):
    def test_parse_fastapi_log(self):
        sample_log = '''
        INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK
        INFO:     192.168.1.100:45678 - "POST /api/auth/login HTTP/1.1" 401 Unauthorized
        '''
        
        expected_output = [
            {
                "client_ip": "127.0.0.1",
                "client_port": "54321",
                "http_method": "GET",
                "endpoint": "/api/users",
                "http_version": "1.1",
                "status_code": "200",
                "status_text": "OK"
            },
            {
                "client_ip": "192.168.1.100",
                "client_port": "45678",
                "http_method": "POST",
                "endpoint": "/api/auth/login",
                "http_version": "1.1",
                "status_code": "401",
                "status_text": "Unauthorized"
            }
        ]

        # Split sample log into lines and test each one
        log_lines = [line.strip() for line in sample_log.strip().splitlines() if line.strip()]
        for i, line in enumerate(log_lines):
            self.assertEqual(parse_fastapi_log(line), expected_output[i])

    def test_parse_invalid_log(self):
        invalid_log = 'INFO: Invalid log entry'
        expected_output = {}
        self.assertEqual(parse_fastapi_log(invalid_log), expected_output)
