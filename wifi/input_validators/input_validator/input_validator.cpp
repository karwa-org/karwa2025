#include "validation.h"
#include <map>

int main(int argc, char *argv[]) {

    InputValidator v(argc, argv);
    int n = v.read_integer("nbr_antenna", 1, (int)1e5);
    v.space();
    int q = v.read_integer("nbr_queries", 1, (int)1e5);
    v.newline();

    std::map<int, bool> cnt;

    v.read_integers("antenna_positions", n, 0, (long long)1e18, Unique); // Already check for newline at the end

    for(int i = 0; i < q; i++) {
        long long val = v.read_integer("query", 0, (long long)1e18);
        if (cnt[val]) {
            v.WA("Expected antennes to have a unique position : " + std::to_string(val) + " is not unique.");
        }
        v.newline();
    }
}
