# shedding.py

Shedding.py is a Python wrapper for the EskomSePush API. It provides a simple interface to the API, and handles all the authentication and session management for you.

## Example

Here is a basic example of us getting an area's information

```py
from shedding import get_area_information

area = get_area_information(
    authorization_token="api.token",
    id="eskde-10-fourwaysext10cityofjohannesburggauteng"
)
print(area) # returns all area information from the City of Johannesburg
print(area["schedule"]["days"]) # returns a list of schedules for each day
```

## Installation

```sh
# Windows
$ py -m pip install shedding.py

# UNIX Systems (Linux/MacOS)
$ python3 -m pip install shedding.py
```

## Links

- [Documentation](https://sheddingpy.rtfd.io)
- [Discord Support Server](https://discord.gg/VTPzbjRFpF)
- [EskomSePush API Documentation](https://documenter.getpostman.com/view/1296288/UzQuNk3E) 