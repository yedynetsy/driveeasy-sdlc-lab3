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

## Running tests locally

Activate the virtual environment and run:

```bash
source .venv/bin/activate
python -m pytest -v
```
