target_include_directories(capable_template_app INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}
)

add_executable (capable_template_app main.cpp
    template_class.cpp
)