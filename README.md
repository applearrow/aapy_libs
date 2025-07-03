# aapy_libs

A collection of utility functions for Python projects.

## Installation

### Using pip

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/applearrow/aapy_libs.git
```

### Using uv

For faster installation with uv:

```bash
uv pip install git+https://github.com/applearrow/aapy_libs.git
```

### Using Poetry

If you're using Poetry in your project:

```bash
poetry add git+https://github.com/applearrow/aapy_libs.git
```

## Usage

After installation, you can import and use the utility functions:

```python
from aapy_libs.module import is_even, is_odd, get_unique_items

# Check if a number is even
print(is_even(4))  # True
print(is_even(5))  # False

# Check if a number is odd
print(is_odd(4))  # False
print(is_odd(5))  # True

# Get unique items while preserving order
items = [1, 2, 2, 3, 4, 1, 5]
unique_items = get_unique_items(items)
print(unique_items)  # [1, 2, 3, 4, 5]
```

## Available Modules

### module.py

Contains basic utility functions:

- `is_even(number)`: Check if a number is even
- `is_odd(number)`: Check if a number is odd
- `get_unique_items(items)`: Get unique items from a list while preserving order

## Development

To set up the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/applearrow/aapy_libs.git
   cd aapy_libs
   ```

2. Install Poetry (if you don't have it already):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

4. Alternatively, use uv for faster dependency management:
   ```bash
   pip install uv
   uv pip install -e .
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Poetry + uv Workflow

This project uses Poetry for dependency management and can be used with uv for faster package installation.

### Working with Poetry

```bash
# Install dependencies
poetry install

# Add a new dependency
poetry add <package-name>

# Add a development dependency
poetry add --group dev <package-name>

# Update dependencies
poetry update

# Build the package
poetry build
```

### Using uv with Poetry

uv is a fast Python package installer and resolver that can work with Poetry:

```bash
# Install uv
pip install uv

# Use uv to install dependencies from requirements.txt
uv pip install -r requirements.txt

# Generate requirements.txt from Poetry
./scripts/generate_requirements.py

# Install the package in development mode
uv pip install -e .
```

### CI/CD Integration

For CI/CD pipelines, you can use either Poetry or uv:

With Poetry:
```bash
poetry install --no-interaction --no-ansi
```

With uv:
```bash
uv pip install -r requirements.txt
```