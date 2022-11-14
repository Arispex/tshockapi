Quick access to TShock REST API using python.

## Endpoints

<details>

<summary>Server</summary>

/status

/tokentest

/v2/token/create

/v2/server/broadcast

/v3/server/rawcmd

/v3/server/motd

/v2/server/off

/v3/server/reload

/v3/server/rules

/v2/server/status

</details>

<details>

<summary>User</summary>

/v2/users/create

/v2/users/destroy

/v2/users/read

/v2/users/list

/v2/users/update

/v2/users/activelist

</details>

<details>

<summary>World</summary>

/v3/world/bloodmoon

/v2/world/butcher

/world/meteor

/world/read

/v2/world/save

</details>

<details>

<summary>Ban</summary>

/v3/bans/create

/v3/bans/destroy

/v3/bans/read

/v3/bans/list

</details>

<details>

<summary>Player</summary>

/v2/players/kick

/v2/players/kill

/v2/players/list

/v2/players/mute

/v4/players/read

/v2/players/unmute

</details>

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