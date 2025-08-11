# =� vibemax

AI-powered maximum finder that uses OpenAI to determine what "max" really means. 

Because sometimes the obvious answer isn't the fun answer! <�

## ( Features

- **AI-powered maximum detection**: Uses OpenAI to intelligently determine what "maximum" means for your data
- **Chaos mode**: 10% of the time, uses the 2nd most obvious interpretation of "max" for unexpected results
- **Flexible input handling**: Automatically converts weird objects to text for AI processing
- **Type validation**: Ensures you're actually passing a list (because vibes require structure)

## <� Quick Start

```bash
pip install vibemax
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-key-here'
```

```python
from vibemax import vibemax

# Numbers - usually picks the largest
numbers = [1, 42, 7, 100, 23]
result = vibemax(numbers)
print(result)  # Probably 100... but maybe not! >7

# Strings - gets creative with "maximum"
words = ["tiny", "HUGE", "medium", "gigantic", "small"]
result = vibemax(words)
print(result)  # Could be "HUGE", "gigantic", or something unexpected!

# Mixed objects - handles anything
mixed = [{"size": 10}, {"size": 100}, "elephant", 42, [1, 2, 3, 4, 5]]
result = vibemax(mixed)
print(result)  # Who knows what the AI will think is "maximum"!
```

## <� How It Works

1. **Validates** your input is actually a list (because we have standards)
2. **Converts** all objects to text representations for AI processing
3. **Asks OpenAI** to find the maximum using its best judgment
4. **10% chaos mode**: Sometimes uses the 2nd most obvious interpretation
5. **Returns** the original object (not the text representation)

## <� The 10% Chaos Factor

Most of the time, vibemax behaves predictably. But 10% of the time, it deliberately chooses the *second* most obvious interpretation of "maximum" to keep things interesting:

- For `[1, 2, 3]`: Usually returns `3`, but might return `2` (second highest)
- For `["a", "bb", "ccc"]`: Usually returns `"ccc"` (longest), but might return `"bb"` (second longest)
- For mixed data: Could prioritize different attributes entirely!

Run the same input multiple times to see the chaos in action! <*

## =� Run the Examples

```bash
git clone https://github.com/o-mike/vibemax.git
cd vibemax
uv run main.py
```

## > Contributing

This is a fun project! Feel free to:
- Add more chaos modes
- Improve object-to-text conversion
- Add more examples
- Make it even more ridiculous

## =� License

MIT License - because vibes should be free!

---

*Inspired by the beautiful absurdity of using AI for trivial tasks.* >(