# DriveEasy — SDLC & CI/CD

Educational project for Laboratory Work No. 3.

## Project
DriveEasy is a car rental management system.

## Goals
- Demonstrate a Git branching strategy
- Implement a small Python booking module
- Add automated tests
- Configure GitHub Actions CI
- Simulate releases and hotfixes

## Technologies
- Python
- pytest
- Git and GitHub
- GitHub Actions

## Release 1.0.0

- Added vehicle booking holds with a 15-minute expiration.
- Prevented duplicate active holds for the same vehicle.
- Allowed a new hold after the previous hold expires.
- Added three automated tests.
- Configured GitHub Actions to run tests on pushes and pull requests.

## Local quality checks and build

Use Python 3.10 or newer. Create and activate a virtual environment, then
install the project with its development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Run the same quality checks used by GitHub Actions:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
```

The test command requires at least 80% coverage of the `driveeasy` package.

Build installable and source packages with:

```bash
python -m build
```

The wheel and source archive appear in `dist/`. In CI, the build runs only
after lint, formatting, tests, and coverage pass. GitHub Actions saves the
packages as a workflow artifact.
