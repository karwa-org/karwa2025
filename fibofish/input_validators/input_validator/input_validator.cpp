#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    v.read_integer("N", 1, (long long)1e18);
    v.newline();
    return 0;
}
