"""
Basic tests for the chadGPT application.
"""
import pytest
import sys
import os

# Add the parent directory to the path so we can import server modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_server_modules_exist():
    """Test that core server module files exist."""
    server_dir = os.path.join(os.path.dirname(__file__), '..', 'server')
    assert os.path.exists(server_dir), "server directory not found"
    
    expected_modules = ['backend.py', 'website.py', 'bp.py', 'config.py', 'babel.py']
    for module in expected_modules:
        module_path = os.path.join(server_dir, module)
        assert os.path.exists(module_path), f"{module} not found in server directory"


def test_config_file_exists():
    """Test that the config.json file exists."""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    assert os.path.exists(config_path), "config.json file not found"


def test_config_file_valid_json():
    """Test that the config.json file contains valid JSON."""
    import json
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    with open(config_path, 'r') as f:
        try:
            config = json.load(f)
            assert isinstance(config, dict), "config.json should contain a JSON object"
        except json.JSONDecodeError as e:
            pytest.fail(f"config.json is not valid JSON: {e}")


def test_requirements_file_exists():
    """Test that the requirements.txt file exists."""
    req_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
    assert os.path.exists(req_path), "requirements.txt file not found"


def test_requirements_file_not_empty():
    """Test that the requirements.txt file is not empty."""
    req_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
    with open(req_path, 'r') as f:
        content = f.read().strip()
        assert len(content) > 0, "requirements.txt is empty"


def test_run_script_exists():
    """Test that the run.py script exists."""
    run_path = os.path.join(os.path.dirname(__file__), '..', 'run.py')
    assert os.path.exists(run_path), "run.py file not found"


def test_run_script_has_main():
    """Test that run.py has a main block."""
    run_path = os.path.join(os.path.dirname(__file__), '..', 'run.py')
    with open(run_path, 'r') as f:
        content = f.read()
        assert "if __name__ == '__main__':" in content, "run.py should have a main block"


def test_client_directory_exists():
    """Test that the client directory exists."""
    client_dir = os.path.join(os.path.dirname(__file__), '..', 'client')
    assert os.path.exists(client_dir), "client directory not found"


def test_g4f_directory_exists():
    """Test that the g4f directory exists."""
    g4f_dir = os.path.join(os.path.dirname(__file__), '..', 'g4f')
    assert os.path.exists(g4f_dir), "g4f directory not found"
