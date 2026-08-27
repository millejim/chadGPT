"""
Basic tests for the FreeGPT WebUI application.
"""
import unittest
import os
import json


class TestProjectStructure(unittest.TestCase):
    """Test that the project structure is correct."""
    
    def test_config_file_exists(self):
        """Test that config.json exists."""
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
        self.assertTrue(os.path.exists(config_path), "config.json file should exist")
    
    def test_config_file_valid_json(self):
        """Test that config.json is valid JSON."""
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            self.assertIsInstance(config, dict)
            self.assertIn('site_config', config, "config should have 'site_config' key")
        except json.JSONDecodeError as e:
            self.fail(f"config.json is not valid JSON: {e}")
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists."""
        req_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
        self.assertTrue(os.path.exists(req_path), "requirements.txt file should exist")
    
    def test_run_script_exists(self):
        """Test that run.py exists."""
        run_path = os.path.join(os.path.dirname(__file__), '..', 'run.py')
        self.assertTrue(os.path.exists(run_path), "run.py file should exist")
    
    def test_server_directory_exists(self):
        """Test that server directory exists."""
        server_path = os.path.join(os.path.dirname(__file__), '..', 'server')
        self.assertTrue(os.path.isdir(server_path), "server directory should exist")
    
    def test_client_directory_exists(self):
        """Test that client directory exists."""
        client_path = os.path.join(os.path.dirname(__file__), '..', 'client')
        self.assertTrue(os.path.isdir(client_path), "client directory should exist")


if __name__ == '__main__':
    unittest.main()
