#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    v.read_integer("N", 0, (int)1e9);
    v.newline();
    v.read_integer("X", 1, (int)1e9);
    v.newline();
    return 0;
}
