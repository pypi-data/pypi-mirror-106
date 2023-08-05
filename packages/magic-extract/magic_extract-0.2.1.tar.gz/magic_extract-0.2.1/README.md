# magic_extract

Based on https://andyljones.com/posts/post-mortem-plotting.html

```python
from magic_extract import extract

def main():
    x = 3
    extract()

main()
print(x)  # prints 3
```

```python
from magic_extract import debug

def main(x):
    y = x - 2
    return x / y  # can DivideByZeroException

debug(main, 4)  # returns 2
debug(main, 3)  # returns 3
debug(main, 2)
print(y)  # prints 0
```
