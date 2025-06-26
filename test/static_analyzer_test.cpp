#include "template_class.h"

bool aFunction() {
    // This function does nothing.
    return true;  // Returns true.
}

bool mainFunction() {
    while (true) {
        TemplateClass obj;
        if (!obj.function2()) {
            return false;
        }

        // do something
    }
}

bool mainFunction2() {
    int i = 0, j = 0;
    while (i < 10) {
        ++j;
    }
}
