cmake_minimum_required(VERSION 3.15)

# Options
option (BUILD_TESTS "Build the tests" ON)

project(
  "Capable cpp template"
  VERSION 0.1.0
  LANGUAGES CXX
)

add_subdirectory(src)

# Add auto-tests
if(BUILD_TESTS)
    enable_testing ()
    include(FetchContent)
    FetchContent_Declare(
      googletest
      URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.tar.gz
    )
    FetchContent_MakeAvailable(googletest)    
    add_subdirectory (test)
endif ()
