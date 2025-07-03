"""
Utility functions module for aapy_libs.
"""

def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if number is even, False otherwise
    """
    return number % 2 == 0

def is_odd(number):
    """
    Check if a number is odd.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if number is odd, False otherwise
    """
    return number % 2 != 0

def get_unique_items(items):
    """
    Return a list of unique items while preserving order.
    
    Args:
        items (list): A list of items
        
    Returns:
        list: A list with duplicate items removed while preserving order
    """
    seen = set()
    return [item for item in items if not (item in seen or seen.add(item))]
