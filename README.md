<p align="center">
  <a href="./resources/icons/main.png" target="blank"><img src="./resources/icons/main.png" width="120" alt="Your Logo" /></a>
</p>
<p align="center">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/dimanikulin/capable-cpp-template">
  <img alt="GitHub followers" src="https://img.shields.io/github/followers/dimanikulin?style=social">
  <img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/dimanikulin/capable-cpp-template">
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/dimanikulin/capable-cpp-template">
  </br>

  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/dimanikulin/capable-cpp-template?include_prereleases">
  <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/dimanikulin/capable-cpp-template/total">
  <img alt="GitHub Release Date" src="https://img.shields.io/github/release-date-pre/dimanikulin/capable-cpp-template">
  </br>
  <a href="https://github.com/dimanikulin/capable-cpp-template/actions/workflows/main.yml"><img src="https://github.com/dimanikulin/capable-cpp-template/actions/workflows/main.yml/badge.svg?branch=master" alt="Tests"/></a>
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/dimanikulin/capable-cpp-template">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/dimanikulin/capable-cpp-template">
  </br>
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/dimanikulin/capable-cpp-template">
  <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/dimanikulin/capable-cpp-template">
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/dimanikulin/capable-cpp-template">
  <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/dimanikulin/capable-cpp-template">
  </br>
  <a href="https://github.com/dimanikulin/capable-cpp-template/projects/1"><img src="https://img.shields.io/badge/roadmap-view-d90368"> </a>
  <img alt="GitHub Discussions" src="https://img.shields.io/github/discussions/dimanikulin/capable-cpp-template">
  <img alt="GitHub" src="https://img.shields.io/github/license/dimanikulin/capable-cpp-template">
  <a href="https://github.com/dimanikulin/capable-cpp-template/edit/master/README.md"><img src="https://img.shields.io/badge/documentation-read-d90368"> </a>
  </br>

</p>

# Quick Links

- [Description](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#description)
- [Features](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#features)
- [Initialization](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#initialization)
- [Building](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#building)
- [Using QT](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#using-qt)
- [Testing](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#testing)
- [Formatting](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#formatting)
- [Static analyzers](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#static-analyzers)
- [Code coverage](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#code-coverage)
- [Documentation](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#documentation)
- [Packaging](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#packaging)
- [Coming Features](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#coming-features)
- [Contributing](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#contributing)
- [Author](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#author)
- [License](https://github.com/dimanikulin/capable-cpp-template?tab=readme-ov-file#license)

# Description

A template for C++ projects using CI, Building, Testing, Formatting, Documenting and more.

Aimed to use starting point with a big number of features with easy way to include or exclude a feature.

This is my POV on such a type of template, thus you might disagree with what I use and how I do things.

And any feedback is really appreciated!

# Features

| # | Feature                 | CI support | Description    |
| - | ------------------------|------------|:--------------:|
|  | License                  | N/A        |  Fully open license. The project is licensed under the [Unlicense](https://unlicense.org/)|
|  | MD templates             | N/A        | Attractive main README (Logo, Badges, Quick Links, Tables, Diagrams), TBD |
|  | Building                 | Yes        | TBD, Use of Ccache to speed up the builds |

# Initialization

There are two options to install the project:

- clone if from [GitHub](https://github.com/dimanikulin/capable-cpp-template)
- [use this repo as template](https://github.com/dimanikulin/capable-cpp-template/generate)

If you would like to clone the repository please run:

```bash
git clone https://github.com/dimanikulin/capable-cpp-template/
```

## Readme.md

You need to provide an icon located at "./resources/icons/main.png" if you wish to use the icon in this README file.

Then you need to updated "href" in badges to refer to your repository. But please notice repo must be public to use badges.

Also in GitHub README.MD you can use *mermaid* to draw different diagrams like in the following example:

```mermaid
flowchart LR
    B -->|Multimedia data| C(Online Multimedia IR system)
    B -->|Multimedia data| D(Offline Multimedia IR system)
    A(Photo Album owner) --> B(FVA Solution)
    A(Photo Album owner) --> D1
    A(Photo Album owner) --> D2
    A(Photo Album owner) --> D3
    D1(fa:fa-tablet Tablet) -->|Multimedia data| B(FVA Solution)
    D2(fa:fa-phone Phone) -->|Multimedia data| B(FVA Solution)
    D3(fa:fa-hdd-o External Disk) -->|Multimedia data| B(FVA Solution)
```

## Building

Then please update `"Project"` in `CMakeLists.txt`

```cmake
project(
  "Project"
  VERSION 0.1.0
  LANGUAGES CXX
)
```

with your project name.

# Building

Locally or on CI
TBD

# Using QT

TBD

# Testing

Locally or on CI
TBD

# Formatting

TBD

# Static analyzers

TBD

# Code coverage

TBD

# Documentation

Locally or on CI

TBD

# Packaging

TBD

# Coming features

- build with Ninja and Cmake(CI)
- CMake configuration
- Documenting using Doxygen and Readme support (CI and Local) with Doxy configuration, Publish of documentation on git hub pages
- Unit testing support, through GoogleTest and CTests (with an option to enable GoogleMock) (CI and Locally) and Publish Test Results
- Using GitHub Actions CI workflows for Windows Linux and MacOS

# Coming features, next

- Using QT (CI and Locally)
- Md Contributing Guideliness, Issues and Pull Requests,
- An example of a Clang-Format config, inspired from the base Google model, with minor tweaks. This is aimed only as a starting point, as coding style is a subjective matter, everyone is free to either delete it (for the LLVM default) or supply their own alternative,
- Static analyzers integration, with Clang-Tidy and Cppcheck(CI and Locally), the former being the default option,
- Code coverage, enabled by using the ENABLE_CODE_COVERAGE option, through Codecov CI integration,
- Package manager support, with Conan and Vcpkg, through their respective options, use Wix for win packages
- use boold and italic
- proofread

# Contributing

TBD

# Author

[Dmytro Nikulin](https://github.com/dimanikulin)

# License

This project is licensed under the [Unlicense](https://unlicense.org/) - see the [LICENSE](https://github.com/dimanikulin/capable-cpp-template?tab=Unlicense-1-ov-file) file for details
