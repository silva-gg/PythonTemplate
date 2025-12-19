"""
Core functionality for your package.

This is an example module. Rename and modify it as needed.
"""

from typing import Optional, Dict, Any


class YourMainClass:
    """
    Main class for your package functionality.
    
    This is a template class that you should customize for your needs.
    
    Attributes:
        name (str): A descriptive name for the instance.
        config (Dict[str, Any]): Configuration dictionary.
    
    Example:
        >>> obj = YourMainClass(name="example")
        >>> result = obj.process(data="test")
        >>> print(result)
        'Processed: test'
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the YourMainClass instance.
        
        Args:
            name: A descriptive name for the instance.
            config: Optional configuration dictionary.
        """
        self.name = name
        self.config = config or {}
    
    def process(self, data: Any) -> str:
        """
        Process the input data.
        
        Args:
            data: Input data to process.
        
        Returns:
            Processed result as a string.
        
        Example:
            >>> obj = YourMainClass(name="processor")
            >>> obj.process("test")
            'Processed: test'
        """
        return f"Processed: {data}"
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get information about this instance.
        
        Returns:
            Dictionary containing instance information.
        """
        return {
            "name": self.name,
            "config": self.config,
        }


def your_utility_function(value: str, uppercase: bool = False) -> str:
    """
    Example utility function.
    
    Args:
        value: Input string value.
        uppercase: Whether to convert to uppercase.
    
    Returns:
        Processed string value.
    
    Example:
        >>> your_utility_function("hello")
        'hello'
        >>> your_utility_function("hello", uppercase=True)
        'HELLO'
    """
    if uppercase:
        return value.upper()
    return value
