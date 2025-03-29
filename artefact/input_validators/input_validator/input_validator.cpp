#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int n = v.read_integer("length", 1, 3000);
    v.newline();
    v.read_integers("elements", n, 1, (int long)1e9);
    return 0;
}
