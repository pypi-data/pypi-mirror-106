# inverterd-client

This is a Python [inverterd](https://github.com/gch1p/inverter-tools) client library.

## Installation

It's available on Pypi:

```
pip install inverterd
```

## Usage example
```python
from inverterd import Client, Format

c = Client(8305, '127.0.0.1')
c.connect()

c.format(Format.JSON)
print(c.exec('get-status'))
print(c.exec('get-year-generated', (2021,)))
```

## License

MIT