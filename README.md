[![Continous Integration](https://github.com/Marcus-K-Thorsen/test_mandatory_one_backend/actions/workflows/ci.yaml/badge.svg)](https://github.com/Marcus-K-Thorsen/test_mandatory_one_backend/actions/workflows/ci.yaml)

# Getting started
1. Install the project
```bash
./install.sh
```

2. Setup .env (replace host, port, username and password if necessary)
```bash
cp .env.example .env
```

3. Setup MySQL (replace host, username and password if necessary)
```bash
mysql -h 127.0.0.1 -u root -p"password" < addresses.sql
```

4. Activate virtual environment
```bash
source venv/bin/activate 2>/dev/null || venv\Scripts\activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null && echo "Virtual environment activated." || echo "Failed to activate virtual environment."
```

5. Start Server
```bash
fastapi dev main.py
```

# Virtual environment
Create a virtual environment and activate it.
Note: This is only necessary when you setup the project.
```bash
python -m venv venv
```

### Activate
Note: This is required before working in the project.
```bash
# UNIX
source venv/bin/activate  

# Windows
venv\Scripts\activate 

# Git Bash Windows
source venv/Scripts/activate 
```

### Verify Virtual Enviroment
```bash
which python
```
Should return a string pointing to the Python binaries stored within `path-to-project/project/venv/bin/python`.

### Deactivate
Leave the virtual environment
```bash
deactivate
```

# Dependencies

### Install
*Note: Ensure you have created and activated the virtual environment first*
```bash
pip install -r requirements.txt
pip install -e .
```

### Update
```bash
python -m pip freeze requirements.txt
```

# Test
Run a single time (https://docs.pytest.org/en/stable/)
```bash
pytest
```

Run with watcher (https://pypi.org/project/pytest-watch/)
```bash
ptw
```

Generate coverage report (https://coverage.readthedocs.io/en/7.6.2/index.html)
```bash
./coverage.sh
```

# Frontend
1. Go to https://github.com/niiicolai/js_fake_info_frontend and download the repository.
2. Download the 'Express' plugin or another web-server plugin for visual code.
3. Start the server by pressing Ctrl+Shift+P, type 'express' and select 'Host: current workspace'

