# Contributing to Sentinel Forge

Thank you for your interest in contributing to Sentinel Forge! This document provides guidelines for contributing to this neurodivergent-aware cognitive AI orchestration platform.

## 🧠 Our Mission
We're building AI that adapts to neurodivergent thinking patterns instead of forcing conformity. Every contribution helps make AI more accessible to diverse cognitive styles.

## 🚀 Ways to Contribute

### Code Contributions
- **Bug fixes** - Help us improve stability and performance
- **New features** - Add cognitive lenses or processing capabilities
- **Documentation** - Improve setup guides, API docs, or examples
- **Tests** - Add test cases for better reliability

### Non-Code Contributions
- **Issue reports** - Found a bug? Let us know!
- **Feature requests** - Have ideas for new cognitive processing?
- **Documentation feedback** - Help us make docs clearer
- **Community support** - Help other users in discussions

## 📋 Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/sentinel-forge-cognitive-orchestrator.git
   cd sentinel-forge-cognitive-orchestrator
   ```
3. **Set up development environment**:
   ```bash
   pip install -r requirements.txt
   # For mock mode (recommended for development)
   echo "MOCK_AI=true" > .env
   ```
4. **Run tests** to ensure everything works:
   ```bash
   pytest tests/
   python scripts/smoke_test.py
   ```

## 🔧 Coding Standards

### Python Guidelines
- **Type hints** required for all functions
- **Docstrings** for public methods using Google style
- **Pydantic models** for data validation
- **Async/await** for I/O operations
- **Descriptive variable names** (no single letters except loops)

### Commit Messages
- Use clear, descriptive commit messages
- Start with verb: "Add", "Fix", "Update", "Refactor"
- Keep first line under 50 characters
- Add body for complex changes

### Testing
- Write tests for new features
- Ensure all tests pass before submitting PR
- Test both mock and live AI modes

## 📝 Pull Request Process

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards

3. **Test thoroughly**:
   ```bash
   pytest tests/
   python scripts/run_full_eval.py
   ```

4. **Update documentation** if needed (README, API docs)

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request** on GitHub:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template
   - Request review

## 🎯 Code Review Process

- All PRs require review before merging
- Be open to feedback and suggestions
- Address review comments promptly
- Keep discussions respectful and constructive

## 🐛 Reporting Issues

When reporting bugs, please include:
- **Clear title** describing the issue
- **Steps to reproduce** the problem
- **Expected vs actual behavior**
- **Environment details** (Python version, OS, etc.)
- **Error messages/logs** if applicable

## 💡 Feature Requests

For new features, please:
- Check if the feature already exists or is planned
- Describe the problem it solves
- Explain how it fits our neurodivergent mission
- Consider implementation complexity

## 📞 Getting Help

- **GitHub Discussions** - General questions and community chat
- **Issues** - Bug reports and feature requests
- **Documentation** - Check the README and docs/ folder first

## 🙏 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment for all cognitive styles
- No discrimination or harassment

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make AI more accessible to all cognitive styles!** 🧠✨

*Built with ❤️ for the neurodivergent community*