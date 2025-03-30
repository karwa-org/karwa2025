#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int n = v.read_integer("nbr_of_lines", 1, 700);
    v.space();
    int m = v.read_integer("nbr_of_columns", 1, 700);
    v.newline();

    int is = v.read_integer("start_line", 0, n-1);
    v.space();
    int js = v.read_integer("start_column", 0, m-1);
    v.space();
    int it = v.read_integer("target_line", 0, n-1);
    v.space();
    int jt = v.read_integer("target_column", 0, m-1);
    v.newline();

    for(int i = 0; i < n; i++) {
        v.read_string("matrix", m, m, "+P");
        v.newline();
    }
}
