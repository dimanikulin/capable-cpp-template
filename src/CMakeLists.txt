add_library(capable_template INTERFACE)

target_include_directories(capable_template
                           INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

target_sources(capable_template INTERFACE template_class.cpp)

install(TARGETS capable_template)
