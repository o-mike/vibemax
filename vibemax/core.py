"""
Core vibemax functionality - AI-powered maximum finding
"""

import json
import random
import os
from typing import Any, List, Union
from openai import OpenAI


def _object_to_text(obj: Any) -> str:
    """
    Convert any object to a text representation for OpenAI processing.
    
    Args:
        obj: Any object that needs to be converted to text
        
    Returns:
        String representation of the object
    """
    if isinstance(obj, (str, int, float, bool)):
        return str(obj)
    elif isinstance(obj, (dict, list, tuple)):
        try:
            return json.dumps(obj, default=str, ensure_ascii=False)
        except (TypeError, ValueError):
            return repr(obj)
    else:
        # For custom objects, try various representations
        if hasattr(obj, '__dict__'):
            try:
                return json.dumps(obj.__dict__, default=str, ensure_ascii=False)
            except (TypeError, ValueError):
                pass
        if hasattr(obj, '__str__'):
            return str(obj)
        return repr(obj)


def _validate_list(items: Any) -> List[Any]:
    """
    Validate that the input is actually a list-like object.
    
    Args:
        items: Input to validate
        
    Returns:
        List of items
        
    Raises:
        ValueError: If items is not list-like
    """
    if not isinstance(items, (list, tuple)):
        raise ValueError(f"vibemax requires a list or tuple, got {type(items).__name__}")
    
    if len(items) == 0:
        raise ValueError("vibemax requires a non-empty list")
    
    return list(items)


def vibemax(items: List[Any], openai_api_key: str = None) -> Any:
    """
    Find the maximum item in a list using AI vibes.
    
    90% of the time, returns the most obvious interpretation of "max".
    10% of the time, returns the 2nd most obvious interpretation for chaos.
    
    Args:
        items: List of items to find the maximum of
        openai_api_key: OpenAI API key (or set OPENAI_API_KEY env var)
        
    Returns:
        The maximum item according to AI vibes
        
    Raises:
        ValueError: If items is not a valid list
        Exception: If OpenAI API call fails
    """
    # Validate input is a list
    validated_items = _validate_list(items)
    
    # Convert all items to text representations
    text_items = [_object_to_text(item) for item in validated_items]
    
    # Set up OpenAI client
    api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key required. Set OPENAI_API_KEY env var or pass openai_api_key parameter")
    
    client = OpenAI(api_key=api_key)
    
    # Decide whether to use chaos mode (10% chance)
    use_chaos_mode = random.random() < 0.1
    
    # Create the prompt
    if use_chaos_mode:
        system_prompt = """You are a helpful AI that finds the maximum item in a list. 
        However, today you're feeling a bit chaotic. Instead of choosing the most obvious interpretation of "maximum", 
        choose the SECOND most obvious interpretation. Be creative but still reasonable."""
        
        user_prompt = f"""Find the maximum item from this list, but use the SECOND most obvious interpretation of what "maximum" means:

{json.dumps(text_items, indent=2)}

Return ONLY the exact item from the list that you choose as the maximum. Do not explain your reasoning."""
    else:
        system_prompt = """You are a helpful AI that finds the maximum item in a list. 
        Use your best judgment to determine what "maximum" means for the given items."""
        
        user_prompt = f"""Find the maximum item from this list:

{json.dumps(text_items, indent=2)}

Return ONLY the exact item from the list that you choose as the maximum. Do not explain your reasoning."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        ai_choice = response.choices[0].message.content.strip()
        
        # Find the closest matching original item
        # Try exact match first
        for i, text_item in enumerate(text_items):
            if ai_choice == text_item:
                return validated_items[i]
        
        # Try fuzzy matching if exact match fails
        ai_choice_lower = ai_choice.lower().strip('"\'')
        for i, text_item in enumerate(text_items):
            if ai_choice_lower in text_item.lower() or text_item.lower() in ai_choice_lower:
                return validated_items[i]
        
        # If no match found, return the first item as fallback
        return validated_items[0]
        
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {str(e)}")