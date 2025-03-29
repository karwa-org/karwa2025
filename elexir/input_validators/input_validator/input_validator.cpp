#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    v.read_integer("target_sum", 1, 42);
    v.space();
    v.read_integer("target_product", 1, (int long)1e9);
    v.newline();
    return 0;
}
