// Copyright {YEAR} YOUR COMPANY NAME.
// All Rights Reserved. The information contained herein is confidential
// property of YOUR COMPANY NAME. The use, copying, transfer or disclosure of such
// information is prohibited except by written agreement with YOUR COMPANY NAME.

#include "template_class.h"

int TemplateClass::function(int param) { return (param); }

bool TemplateClass::function2() {
    if (function(0) == 0) return false;
    if (function(1) == 0) return false;
    if (function(2) == 0) return false;

    return true;
}
