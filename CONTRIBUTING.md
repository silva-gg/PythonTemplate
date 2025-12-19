# Contributing to Your Package

Thank you for considering contributing to this project! We welcome contributions of all kinds.

## How to Contribute

### Reporting Bugs

1. **Check existing issues** to see if the bug has already been reported
2. **Create a new issue** with:
   - Clear, descriptive title
   - Steps to reproduce the bug
   - Expected behavior
   - Actual behavior
   - Your environment (OS, Python version)
   - Any relevant code snippets or error messages

### Suggesting Enhancements

1. **Check existing issues** for similar suggestions
2. **Create a new issue** describing:
   - The enhancement you'd like to see
   - Why it would be useful
   - How it might work
   - Any alternatives you've considered

### Pull Requests

1. **Fork the repository**
2. **Create a new branch** from `develop`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**:
   - Write clear, concise code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**:
   ```bash
   pytest tests/ -v
   black src/your_package --line-length 100
   flake8 src/your_package --max-line-length=100
   ```

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```
   
   Use conventional commit messages:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `test:` Adding tests
   - `refactor:` Code refactoring
   - `style:` Formatting changes
   - `chore:` Maintenance tasks

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** against the `develop` branch

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/your-package.git
   cd your-package
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```

4. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

## Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use [Black](https://black.readthedocs.io/) for code formatting (100 character line length)
- Use type hints where appropriate
- Write docstrings for all public functions/classes (Google style)
- Keep functions small and focused

## Testing

- Write tests for all new functionality
- Aim for high test coverage (>80%)
- Use descriptive test names
- Mock external dependencies
- Separate unit tests from integration tests

## Documentation

- Update README.md if you change functionality
- Add docstrings to new functions/classes
- Update CHANGELOG.md with your changes
- Consider adding examples for new features

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
