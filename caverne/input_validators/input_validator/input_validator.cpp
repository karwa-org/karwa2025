#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int h = v.read_integer("cave_height", 1, (int)1e3);
    v.space();
    int l = v.read_integer("cave_width", 1, (int)1e3);
    v.space();
    int p = v.read_integer("cave_depth", 1, (int)1e3);
    v.newline();

    for(int i = 0; i < 2*l; i++) {
        // Default tag: arbitrary (eg increasing, unique)
        // Default sep: space, otherwise newline
        // newline is implicit at the end
        v.read_integers("rock_height", p, 0, h);
    }
    return 0;
}
