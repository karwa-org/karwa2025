#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int c = v.read_integer("nbr_of_vertices", 1, 100000);
    v.newline();
    int d = v.read_integer("post_office_position", 0, c-1);
    v.newline();
    int r = v.read_integer("nbr_of_edges", 0, 100000);
    v.newline();

    for(int i = 0; i < r; i++) {
        int a = v.read_integer("edge_start", 0, c-1);
        v.space();
        int b = v.read_integer("edge_end", 0, c-1);
        v.newline();
        //if (a == b) {
        //    v.WA("Invalid input: Loops are forbidden.");
        //    return 43;
        //}
    }
    return 0;
}
