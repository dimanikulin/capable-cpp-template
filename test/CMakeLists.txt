add_executable (capable_template_app_test
    template_class_test.cpp 
	static_analyzer_test.cpp
)

target_link_libraries(capable_template_app_test 
			PUBLIC gtest gtest_main gmock
                    	PUBLIC capable_template
) 

add_test(capable_template_app_test capable_template_app_test)

