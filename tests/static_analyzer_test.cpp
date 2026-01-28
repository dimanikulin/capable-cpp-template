// Copyright {YEAR} YOUR COMPANY NAME.
// All Rights Reserved. The information contained herein is confidential
// property of YOUR COMPANY NAME. The use, copying, transfer or disclosure of such
// information is prohibited except by written agreement with YOUR COMPANY NAME.

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
