#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int n = v.read_integer("nbr_of_artifacts", 1, 300);
    v.newline();
    v.read_integers("elements", n, 1, (int long)1e9);
}
