
# Contributing to Numainda

Thank you for your interest in contributing to Numainda! Your contributions are highly valued and crucial for the success of this project. This document outlines the standards and best practices for contributing.

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. **Fork the Repository**: Fork the main Numainda repository to your GitHub account.

2. **Clone the Fork**: Clone your fork locally on your machine.

   ```
   git clone https://github.com/yourusername/numainda.git
   ```

3. **Set Upstream**: Add the original repository as an upstream remote.

   ```
   git remote add upstream https://github.com/originalusername/numainda.git
   ```

## Development Workflow

1. **Sync Your Fork**: Before you start, make sure your fork is up-to-date with the main repository.

   ```
   git pull upstream main
   ```

2. **Create a Branch**: Create a new branch for each feature, bugfix, or documentation improvement.

   ```
   git checkout -b feature/your-feature-name
   ```

3. **Write Code**: Write your code, following the coding standards and guidelines described below.

4. **Commit Changes**: Make frequent, smaller commits with clear and descriptive messages.

   ```
   git add .
   git commit -m "Your descriptive commit message"
   ```

5. **Push to Fork**: Push your changes to your fork on GitHub.

   ```
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**: Go to your fork on GitHub and create a new pull request.

## Coding Standards

- Follow PEP 8 for Python code.
- Use meaningful variable and function names.
- Comment your code for clarity.
- Write unit tests for your features.

## Testing

Run tests to make sure your code is working as expected and does not break existing functionality.

```
pytest tests/
```

## Pull Request Guidelines

- PRs should have a clear title and description.
- Make sure your PR is up-to-date with the main repository.
- Squash insignificant commits.
- Include relevant issue numbers in your PR.

## Review Process

1. A core contributor will review your PR.
2. Changes may be requested for clarity, performance, or adherence to standards.
3. Once approved, your PR will be merged.

## Recognition

All contributors will be recognized in the project's README or a separate CONTRIBUTORS file.
