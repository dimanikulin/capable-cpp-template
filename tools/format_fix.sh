#!/bin/bash
# Copyright {YEAR} YOUR COMPANY NAME.
# All Rights Reserved. The information contained herein is confidential
# property of YOUR COMPANY NAME. The use, copying, transfer or disclosure of such
# information is prohibited except by written agreement with YOUR COMPANY NAME.

find tests -regex '.*\.\(cpp\|h\|cc\|cxx\)' -exec clang-format-17 -i {} \;
find src -regex '.*\.\(cpp\|h\|cc\|cxx\)' -exec clang-format-17 -i {} \;
