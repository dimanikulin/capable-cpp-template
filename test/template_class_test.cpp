#include "template_class.h"

#include <gtest/gtest.h>

TEST(TemplateClassTest, FunctionReturnsInput) {
    TemplateClass obj;
    EXPECT_EQ(obj.function(5), 5);
    EXPECT_EQ(obj.function(-3), -3);
    EXPECT_EQ(obj.function(0), 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
