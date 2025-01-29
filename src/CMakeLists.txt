target_include_directories(capable_template_app INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}
    )

target_sources(capable_template_app INTERFACE 
        template_class.cpp
        )
