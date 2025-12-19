# Python Package Template

A professional Python package template with complete structure, testing, and CI/CD setup.

## Features

- ✅ Modern Python packaging with `pyproject.toml`
- ✅ Comprehensive test suite with pytest
- ✅ CI/CD with GitHub Actions
- ✅ Documentation structure
- ✅ Code quality tools (black, flake8, mypy)
- ✅ Type hints support
- ✅ Easy PyPI publishing

## Quick Start

1. **Use this template** (on GitHub, click "Use this template")

2. **Clone your new repository**
   ```bash
   git clone https://github.com/your-org/your-package.git
   cd your-package
   ```

3. **Customize for your project**
   - Replace `your_package` with your actual package name in:
     - `pyproject.toml`
     - `setup.py`
     - `src/` folder name
     - `tests/` imports
   - Update author information
   - Update package description
   - Update README.md content

4. **Install in development mode**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

5. **Run tests**
   ```bash
   pytest tests/ -v
   ```

## Project Structure

```
your-package/
├── .github/
│   └── workflows/
│       └── tests.yml           # CI/CD configuration
├── src/
│   └── your_package/
│       ├── __init__.py         # Package initialization
│       └── core.py             # Main code (rename as needed)
├── tests/
│   ├── test_core.py            # Unit tests
│   └── test_integration.py     # Integration tests (optional)
├── .gitignore                   # Git ignore rules
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # Contribution guidelines
├── DEVELOPMENT.md               # Development guide
├── LICENSE                      # MIT License (change if needed)
├── MANIFEST.in                  # Package manifest
├── pyproject.toml              # Modern packaging config
├── README.md                    # Main documentation
├── requirements.txt             # Dependencies
└── setup.py                     # Setup script
```

## Customization Checklist

- [ ] Rename `your_package` folder in `src/`
- [ ] Update `pyproject.toml` with your package details
- [ ] Update `setup.py` with your package name
- [ ] Update `README.md` with your project description
- [ ] Update `LICENSE` if not using MIT
- [ ] Update author information in all files
- [ ] Add your dependencies to `requirements.txt`
- [ ] Update `CHANGELOG.md` with your first version
- [ ] Write your actual code in `src/your_package/`
- [ ] Write tests in `tests/`
- [ ] Update GitHub repository URL in `pyproject.toml`

## Development Workflow

### Install Dependencies
```bash
pip install -e ".[dev]"
```

### Run Tests
```bash
# All tests
pytest tests/ -v

# With coverage
pytest --cov=your_package --cov-report=html

# Specific test file
pytest tests/test_core.py -v
```

### Code Quality
```bash
# Format code
black src/your_package --line-length 100

# Lint
flake8 src/your_package --max-line-length=100

# Type checking
mypy src/your_package
```

### Build Package
```bash
pip install build
python -m build
```

### Publish to PyPI
```bash
pip install twine

# Test PyPI first
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

## Adding Your Code

1. **Write your code** in `src/your_package/`
2. **Add tests** in `tests/`
3. **Update documentation** in README.md
4. **Add to CHANGELOG.md**

Example structure:
```python
# src/your_package/core.py
class YourClass:
    def __init__(self):
        pass
    
    def your_method(self):
        return "Hello World"

# src/your_package/__init__.py
from .core import YourClass
__version__ = "0.1.0"
__all__ = ["YourClass"]
```

## Installation Methods

Your users can install your package in several ways:

### From PyPI (after publishing)
```bash
pip install your-package
```

### From GitHub
```bash
pip install git+https://github.com/your-org/your-package.git
```

### From Source
```bash
git clone https://github.com/your-org/your-package.git
cd your-package
pip install -e .
```

## GitHub Actions CI/CD

The template includes automatic testing on:
- Python versions: 3.7, 3.8, 3.9, 3.10, 3.11
- Triggers: Push to main/develop, Pull requests
- Includes: Linting, testing, coverage

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

**Happy coding! 🚀**

Delete this section and customize the rest for your specific package.
