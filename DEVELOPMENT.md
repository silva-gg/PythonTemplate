# Development Guide

This guide covers the development workflow for this package.

## Initial Setup

### 1. Clone and Install

```bash
git clone https://github.com/your-org/your-package.git
cd your-package
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### 2. Verify Installation

```bash
python -c "import your_package; print(your_package.__version__)"
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=your_package --cov-report=html

# Run specific test file
pytest tests/test_core.py -v

# Run specific test
pytest tests/test_core.py::test_specific_function -v

# Run only integration tests (skipped by default)
pytest tests/test_integration.py -v -m integration
```

### Code Quality

```bash
# Format code
black src/your_package --line-length 100

# Check formatting without changes
black --check src/your_package --line-length 100

# Lint code
flake8 src/your_package --max-line-length=100

# Type checking
mypy src/your_package
```

### Pre-commit Checks

Before committing, run:

```bash
# Format
black src/your_package tests/ --line-length 100

# Lint
flake8 src/your_package --max-line-length=100

# Test
pytest tests/ -v

# Type check
mypy src/your_package
```

## Building and Publishing

### 1. Update Version

Update version in:
- `pyproject.toml` (`version = "x.y.z"`)
- `src/your_package/__init__.py` (`__version__ = "x.y.z"`)
- `CHANGELOG.md` (add release notes)

### 2. Build Package

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Verify build
ls dist/
```

### 3. Test on TestPyPI

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ your-package
```

### 4. Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Verify
pip install your-package
```

### 5. Create GitHub Release

1. Tag the release:
   ```bash
   git tag -a v0.1.0 -m "Release version 0.1.0"
   git push origin v0.1.0
   ```

2. Create release on GitHub with changelog

## Project Structure

```
your-package/
├── src/
│   └── your_package/          # Source code
│       ├── __init__.py        # Package initialization
│       └── core.py            # Main module
├── tests/
│   ├── test_core.py           # Unit tests
│   └── test_integration.py    # Integration tests
├── .github/workflows/
│   └── tests.yml              # CI/CD configuration
├── pyproject.toml             # Package metadata
├── setup.py                   # Setup script
└── README.md                  # Documentation
```

## Common Tasks

### Adding a New Module

1. Create `src/your_package/new_module.py`
2. Add imports to `src/your_package/__init__.py`
3. Create `tests/test_new_module.py`
4. Document in README.md

### Adding Dependencies

1. Add to `dependencies` in `pyproject.toml`
2. Add to `requirements.txt`
3. Update `README.md` if user-facing

### Updating Documentation

1. Update README.md for user-facing changes
2. Update docstrings in code
3. Update CHANGELOG.md
4. Consider adding examples

## Debugging

### Interactive Testing

```python
# Start Python REPL
python

# Import your package
from your_package import YourMainClass

# Test interactively
obj = YourMainClass(name="test")
obj.process("data")
```

### Using pdb

```python
# Add breakpoint in code
import pdb; pdb.set_trace()

# Or use Python 3.7+ built-in
breakpoint()
```

### Verbose Testing

```bash
# Run with print statements
pytest tests/ -v -s

# Run with logging
pytest tests/ -v --log-cli-level=DEBUG
```

## Continuous Integration

The GitHub Actions workflow runs:
- Python 3.7, 3.8, 3.9, 3.10, 3.11
- Linting (flake8)
- Formatting check (black)
- Type checking (mypy)
- Tests with coverage

## Troubleshooting

### Import Errors

```bash
# Reinstall in development mode
pip install -e .
```

### Test Failures

```bash
# Run with verbose output
pytest tests/ -vv -s
```

### Build Errors

```bash
# Clean build artifacts
rm -rf build/ dist/ *.egg-info
python -m build
```

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Code Formatter](https://black.readthedocs.io/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Semantic Versioning](https://semver.org/)
