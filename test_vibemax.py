"""
Simple tests for vibemax functionality
"""

import pytest
from vibemax import vibemax
from vibemax.core import _object_to_text, _validate_list


def test_validate_list():
    """Test list validation"""
    # Valid lists
    assert _validate_list([1, 2, 3]) == [1, 2, 3]
    assert _validate_list((1, 2, 3)) == [1, 2, 3]
    
    # Invalid inputs
    with pytest.raises(ValueError):
        _validate_list("not a list")
    
    with pytest.raises(ValueError):
        _validate_list([])  # empty list


def test_object_to_text():
    """Test object to text conversion"""
    # Basic types
    assert _object_to_text(42) == "42"
    assert _object_to_text("hello") == "hello"
    assert _object_to_text(3.14) == "3.14"
    assert _object_to_text(True) == "True"
    
    # Complex types
    assert '"a": 1' in _object_to_text({"a": 1})
    assert "1" in _object_to_text([1, 2, 3])
    
    # Custom object
    class TestObj:
        def __init__(self):
            self.value = 42
    
    obj = TestObj()
    text = _object_to_text(obj)
    assert "42" in text


def test_vibemax_validation():
    """Test that vibemax validates inputs properly"""
    # Should raise error for non-list
    with pytest.raises(ValueError):
        vibemax("not a list", "fake-api-key")
    
    # Should raise error for empty list  
    with pytest.raises(ValueError):
        vibemax([], "fake-api-key")
    
    # Should raise error for missing API key
    with pytest.raises(ValueError):
        vibemax([1, 2, 3])


# Integration tests would require a real API key
def test_vibemax_with_mock():
    """Test vibemax with mocked OpenAI response"""
    # This would require mocking the OpenAI client
    # Left as an exercise for more comprehensive testing
    pass


if __name__ == "__main__":
    print("Running basic tests...")
    test_validate_list()
    test_object_to_text()
    test_vibemax_validation()
    print("✅ All basic tests passed!")