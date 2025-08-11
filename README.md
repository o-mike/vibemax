# vibemax

An AI-powered `max()` function.

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
# 'JavaScript'

vibemax([True, False, None, 0, '', 'something'])
# 'something'
```