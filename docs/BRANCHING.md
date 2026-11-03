# Git branching strategy

DriveEasy uses GitFlow because the lab simulates planned releases and urgent
fixes. Each branch has a distinct role.

| Branch | Purpose | Merges into |
| --- | --- | --- |
| `main` | Released, stable versions | — |
| `develop` | Integration of completed work | `release/*` |
| `feature/*` | New features and CI improvements | `develop` |
| `release/*` | Final preparation of a version | `main` and `develop` |
| `hotfix/*` | Urgent correction of a released version | `main` and `develop` |

## Release process

1. Create a `feature/*` branch from `develop`.
2. Open a pull request to `develop` after the quality checks pass.
3. Create a `release/*` branch from `develop` to prepare a version.
4. Merge the release into `main` and add an annotated version tag.
5. Merge the release back into `develop` to keep both branches in sync.

For an urgent fix, create `hotfix/*` from `main`, merge it into `main`,
add an annotated patch-version tag, and merge the fix into `develop`.

## Release simulation in this repository

- PR #1 merged `feature/booking-hold` into `develop`.
- PR #2 merged `release/1.0.0` into `main`; tag `v1.0.0` marks that release.
- PR #3 merged `release/1.0.0` back into `develop`.
- PR #4 merged `hotfix/vehicle-id-validation` into `main`; tag `v1.0.1`
  marks the corrected release.
- PR #5 merged the hotfix into `develop`.

## Inspecting the history

```bash
git log --graph --oneline --decorate --all
git tag -n
```
