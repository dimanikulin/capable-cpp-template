# Capable cpp template

A template for C++ projects using CI, Building, Testing, Formatting, Documenting and more
Aimed to use starting point with a big number of features with easy way to include or exclude a feature.

This is my POV on such a type of template, thus you might disagree with what I use and how I do things.
And any feedback is really appreciated!

# Ready features

- Fully open license. The project is licensed under the [Unlicense](https://unlicense.org/)

# Coming features

- badges

- Modern CMake configuration and project, which, to the best of my knowledge, uses the best practices,

- An example of a Clang-Format config, inspired from the base Google model, with minor tweaks. This is aimed only as a starting point, as coding style is a subjective matter, everyone is free to either delete it (for the LLVM default) or supply their own alternative,

- Static analyzers integration, with Clang-Tidy and Cppcheck, the former being the default option,

- Doxygen support, through the ENABLE_DOXYGEN option, which you can enable if you wish to use it,

- Unit testing support, through GoogleTest (with an option to enable GoogleMock) or Catch2,

- Code coverage, enabled by using the ENABLE_CODE_COVERAGE option, through Codecov CI integration,

- Package manager support, with Conan and Vcpkg, through their respective options

- CI workflows for Windows, Linux and MacOS using GitHub Actions, making use of the caching features, to ensure minimum run time,

- .md templates for: README, Contributing Guideliness, Issues and Pull Requests,

- Options to build as a header-only library or executable, not just a static or shared library.

- Ccache integration, for speeding up rebuild times
