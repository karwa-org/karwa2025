#include "validation.h"

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    long long n = v.read_integer("n", 1, 2*(long long)1e5);
    v.space();
    long long q = v.read_integer("q", 1, 2*(long long)1e5);
    v.newline();

    v.read_integers("a", n, 0, (long long)1e18, Unique); // Already check for newline at the end

    for(int i = 0; i < q; i++) {
        long long val = v.read_integer("ai", 0, (long long)1e18);
        v.newline();
    }
   return 0;
}
