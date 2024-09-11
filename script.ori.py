import os

# Set the base path
base_path = r'C:\Users\vijay\Downloads\ops'

# Define the directory structure
dirs = [
    'src',
    'src/mongodb_connect',
    'src/tests',
    'src/tests/integration',
    'src/tests/unit',
    'experiments',
    '.github/workflows'
]

# Define the files to be created
files = [
    'src/mongodb_connect/__init__.py',
    'src/mongodb_connect/mongo_crud.py',
    'src/tests/integration/__init__.py',
    'src/tests/unit/__init__.py',
    '.gitignore',
    'init_setup.sh',
    'pyproject.toml',
    'requirements.txt',
    'requirements-dev.txt',
    'tox.ini',
    'experiments/experiments.ipynb',
    '.github/workflows/python-publish.yml',
    '.github/workflows/ci.yaml',
    'setup.cfg',
    'README.md',
    'template.py'
]

# Create the directories
for dir in dirs:
    os.makedirs(os.path.join(base_path, dir), exist_ok=True)

# Create the files
for file in files:
    with open(os.path.join(base_path, file), 'w') as f:
        f.write('')

print(f"Directories and files have been created in {base_path}.")

