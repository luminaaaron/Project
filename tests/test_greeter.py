#### `test_greeter.py`:
```python
from src.greeter import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
```
