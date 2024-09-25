
# TO-DO
- [Generate random addresses](https://github.com/Marcus-K-Thorsen/test_mandatory_one_backend/blob/main/src/data/fake_person.py#L79-L95)
- [Generate random phone numbers](https://github.com/Marcus-K-Thorsen/test_mandatory_one_backend/blob/main/src/data/fake_person.py#L97-L106)
- Unit and integration tests

# Development

## Virtual environment
Create a virtual environment and activate it:
```
python -m venv venv
```

Activate:
```
source venv/bin/activate  # UNIX
venv\Scripts\activate # Windows
```

Verify it is active:
```
which python
```
Should return a string pointing to the Python binaries stored within `path-to-project/project/venv/bin/python`.

## Install dependencies
*Note: Ensure you have created and activated the virtual environment first*
```
pip install -r requirements.txt
```

## Start Server
```
   fastapi dev main.py
```

## Frontend
1. Go to https://github.com/niiicolai/js_fake_info_frontend and download the repository.
2. Download the 'Express' plugin or another web-server plugin for visual code.
3. Start the server by pressing Ctrl+Shift+P, type 'express' and select 'Host: current workspace'

