# Print line

Setup wheel.exe/twine.exe as your environment path (d:\Python39\Scripts)

## Upload package
```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Examples of how to use

Set configuration

```python
from abqos import set

#set(<file>)
set("1.txt")

```
