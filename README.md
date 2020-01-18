# PyNeutralino

PyNeutralino is a little Python module for making simple HTML/JS GUI apps with Flask.

PyNeutralino is based on [Neutralinojs](https://github.com/neutralinojs/neutralinojs). So PyNeutralino inherits its lightweight and cross platform advantages. If you are familiar with Python and Flask, this would be a good solution for writing cross-platform applications.

## Installing

    pip install PyNeutralino

## A Simple Example

```python
# app.py

from flask import Flask
from pyneutralino import PyNeutralino
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    pn = PyNeutralino(app, name="myapp", port=9000)
    pn.width = 1000
    pn.height = 700
    pn.run()
```

```bash
python app.py
```

## Supports

- Python2 >= 2.7
- Python3 >= 3.4

## Platform

- macOS
- Linux
- Windows