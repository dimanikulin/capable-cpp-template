add_executable (capable_template_app_test
    template_class_test.cpp
)

target_link_libraries(capable_template_app_test PRIVATE gmock_main
                    PUBLIC capable_template
) 

add_test(capable_template_app_test capable_template_app_test)

