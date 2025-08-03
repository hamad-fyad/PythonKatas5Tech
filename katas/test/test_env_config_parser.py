import unittest
from katas.env_config_parser import parse_env_config


class Test_env_config_parser(unittest.TestCase):
    def test_parse_env_config(self):
        sample_env = """
# Database Configuration
DATABASE_URL=postgresql://user:pass@localhost:5432/appdb
DATABASE_POOL_SIZE=10

# Application Settings      
APP_NAME="E-Commerce API"
DEBUG=false
PORT=3000
WORKERS=4

# Feature Flags
ENABLE_LOGGING=true
ENABLE_CACHE="false"
CACHE_TTL=3600

# Empty line above should be ignored
REDIS_URL=redis://localhost:6379/0
"""
        expected_config = {
            "DATABASE_URL": "postgresql://user:pass@localhost:5432/appdb",
            "DATABASE_POOL_SIZE": 10,
            "APP_NAME": "E-Commerce API",
            "DEBUG": False,
            "PORT": 3000,
            "WORKERS": 4,
            "ENABLE_LOGGING": True,
            "ENABLE_CACHE": False,
            "CACHE_TTL": 3600,
            "REDIS_URL": "redis://localhost:6379/0"
        }

        config = parse_env_config(sample_env)
        self.assertEqual(config, expected_config)

    def test_parse_empty_env(self):
        sample_env = ""
        expected_config = {}

        config = parse_env_config(sample_env)
        self.assertEqual(config, expected_config)
    def test_parse_invalid_env(self):
        sample_env = "invalid env"
        expected_config = {}

        config = parse_env_config(sample_env)
        self.assertEqual(config, expected_config)

    def test_parse_empty_line(self):
        sample_env = "\n"
        expected_config = {}

        config = parse_env_config(sample_env)
        self.assertEqual(config, expected_config)

    def test_parse_comment_line(self):
        sample_env = "# This is a comment\n"
        expected_config = {}

        config = parse_env_config(sample_env)
        self.assertEqual(config, expected_config)

        
