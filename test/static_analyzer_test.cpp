bool aFunction() {
    // This function does nothing.
    return true; // Returns true.
}

bool mainFunction() {
    while (true) {
        if (!aFunction()) {
            return false;
        }

        // do something
    }
}

