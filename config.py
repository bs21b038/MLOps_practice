import yaml
import os
from typing import Dict, Any

class Config:
    """Load and manage configuration from config.yaml"""
    
    _instance = None
    _data: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """Load config from config.yaml"""
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        try:
            with open(config_path, "r") as f:
                self._data = yaml.safe_load(f) or {}
            print(f"✓ Config loaded from {config_path}")
        except FileNotFoundError:
            print(f"✗ config.yaml not found at {config_path}")
            self._data = {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get config value by dot notation: 'server.port' or 'api.title'"""
        keys = key.split(".")
        value = self._data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def get_server_config(self) -> Dict[str, Any]:
        """Get server configuration"""
        return self._data.get("server", {})
    
    def get_api_config(self) -> Dict[str, Any]:
        """Get API configuration"""
        return self._data.get("api", {})
    
    def get_endpoints_config(self) -> Dict[str, Any]:
        """Get endpoints configuration"""
        return self._data.get("endpoints", {})


# Singleton instance
config = Config()
