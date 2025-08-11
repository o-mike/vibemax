# vibemax

An AI-powered `max()` function. Because why use `max()` when you can ask GPT what's biggest?

## Installation

```bash
pip install vibemax
export OPENAI_API_KEY='your-key-here'
```

## Usage

```python
from vibemax import vibemax

vibemax([1, 2, 3, 4, 5])
# 5

vibemax(['short', 'medium', 'supercalifragilisticexpialidocious'])
# 'supercalifragilisticexpialidocious'

vibemax(['🐭', '🐘', '🦕'])  
# '🦕'

vibemax([{'name': 'ant', 'size': 1}, {'name': 'elephant', 'size': 100}])
# {'name': 'elephant', 'size': 100}

vibemax(['whisper', 'SHOUT', 'scream'])
# 'SHOUT'

vibemax([1.1, 2.2, 3.3, 99.9])
# 99.9

vibemax(['Python', 'Java', 'JavaScript', 'Go'])
# 'JavaScript' (or maybe 'Python' - depends on the AI's mood!)

vibemax([True, False, None, 0, '', 'something'])
# 'something'
```

## The Chaos Factor

90% of the time, vibemax works exactly like you'd expect.

10% of the time, it picks the *second* most obvious choice. Because why not? 🎲

## How it works

1. Validates input is a list
2. Converts everything to text for the AI
3. Asks OpenAI to pick the maximum
4. Sometimes chaos mode kicks in for fun
5. Returns the original object

Basically `max()` but with ✨ vibes ✨