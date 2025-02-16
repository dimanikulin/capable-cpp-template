cmake_minimum_required(VERSION 3.15)

# Options
option (BUILD_TESTS "Build the tests" ON)
option (ENABLE_COVERAGE "Enable code coverage" ON)

project(
  "Capable cpp template"
  VERSION 0.1.0
  LANGUAGES CXX
)

message(STATUS "CMake version: ${CMAKE_VERSION}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "C++ compiler: ${CMAKE_CXX_COMPILER}")
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Project name: ${PROJECT_NAME}")
message(STATUS "Project version: ${PROJECT_VERSION}")
message(STATUS "Project source dir: ${PROJECT_SOURCE_DIR}")
message(STATUS "Project binary dir: ${PROJECT_BINARY_DIR}")

message(STATUS "Build tests: ${BUILD_TESTS}")
message(STATUS "Enable coverage: ${ENABLE_COVERAGE}")

add_subdirectory(src)

# Code coverage
if(ENABLE_COVERAGE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g -fprofile-arcs -ftest-coverage")
    message("Code coverage is enabled and provided with GCC.")
endif()

# Add auto-tests
if(BUILD_TESTS)
    message(STATUS "Build unit tests for the project. Tests should always be found in the test folder\n")
    enable_testing ()
    include(FetchContent)
    FetchContent_Declare(
      googletest
      URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.tar.gz
    )
    FetchContent_MakeAvailable(googletest)    
    add_subdirectory (test)
endif ()
