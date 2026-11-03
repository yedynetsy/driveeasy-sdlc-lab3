# Changelog

## Unreleased

### Added
- Ruff checks for lint and formatting in CI.
- Test coverage gate requiring at least 80% coverage.
- Python build job producing wheel and source distribution artifacts.
- Documentation of the Git branching strategy.

## v1.0.1

### Fixed
- Rejected blank vehicle IDs, including IDs made only of spaces.
- Added a regression test for blank vehicle IDs.

## v1.0.0

### Added
- Booking holds with a 15-minute expiration.
- Protection against overlapping active holds for the same vehicle.
- Ability to create a new hold after the previous one expires.
- Initial automated tests and GitHub Actions test workflow.
