"""
Example usage of vibemax
"""

import os
from vibemax import vibemax


def main():
    print("🚀 Welcome to vibemax - AI-powered maximum finder!")
    print()
    
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Please set your OPENAI_API_KEY environment variable")
        print("   export OPENAI_API_KEY='your-key-here'")
        return
    
    # Example 1: Numbers
    numbers = [1, 42, 7, 100, 23]
    print(f"📊 Numbers: {numbers}")
    try:
        result = vibemax(numbers)
        print(f"   AI thinks max is: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    # Example 2: Strings
    words = ["tiny", "HUGE", "medium", "gigantic", "small"]
    print(f"📝 Words: {words}")
    try:
        result = vibemax(words)
        print(f"   AI thinks max is: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    # Example 3: Mixed objects
    mixed = [{"size": 10}, {"size": 100}, "elephant", 42, [1, 2, 3, 4, 5]]
    print(f"🎭 Mixed objects: {mixed}")
    try:
        result = vibemax(mixed)
        print(f"   AI thinks max is: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    print("💫 Remember: 10% of the time, vibemax uses the 2nd most obvious interpretation!")
    print("   Run multiple times to see the chaos! 🎲")


if __name__ == "__main__":
    main()
