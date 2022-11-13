Quick access to TShock REST API using python.

## Example

```python
import tshockapi  # Import the tshockapi module

server = tshockapi.Server(host="127.0.0.1", port=7878, token="1234567890")  # Create a server object
print(server.v3_server_rawcmd(cmd="/who"))  # Print the result of the /who command
# {'status': '200', 'response': ['There are currently no players online.']}
```

## Installation

### Windows

```bash
pip install tshockapi
```

### Linux

```bash
pip3 install tshockapi
```