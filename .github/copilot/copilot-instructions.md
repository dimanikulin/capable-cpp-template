# Copilot Instructions

This repository is a C++ CMake template project.

## Project focus

- Keep changes small, explicit, and testable.
- Preserve existing public interfaces unless the task asks for API changes.
- Prefer portable C++ and cross-platform CMake.

## Coding rules

- Follow the existing formatting style in the file being edited.
- Avoid broad refactors in bug-fix pull requests.
- Add or update unit tests in `tests/` when behavior changes.
- Keep includes minimal and avoid unused dependencies.

## Build and test expectations

- Configure with CMake and build with standard targets.
- Run unit tests via CTest when tests are affected.
- Keep warnings low and do not introduce obvious analyzer issues.

## Documentation

- Update README or code comments when behavior or usage changes.
- Keep docs concise and aligned with implementation.
