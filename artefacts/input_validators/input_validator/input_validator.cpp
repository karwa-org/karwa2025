#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    v.read_integer("length", 1, 3000);
    v.newline();
    v.read_integers("elements", n, 1, 3000);
    return 0;
}
