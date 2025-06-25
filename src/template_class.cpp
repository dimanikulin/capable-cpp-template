#include "template_class.h"

int TemplateClass::function(int param) { return param; }

bool TemplateClass::function2() {
    if (function(0) == 0) 
        return false; 
    if (function(1) == 0) 
        return false; 
    if (function(2) == 0) 
        return false; 

     return true;
}