#include "validation.h"
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    std::ifstream ans(argv[2]); // Only for custom checker.

    OutputValidator v(argc, argv);

    long long n, q; in >> n >> q;
    vector<long long> a(n);
    for(auto& i : a) {
        in >> i;
    }

    for(int i = 0; i < q; i++) {

        long long pos; in >> pos;
        long long jury_output; ans >> jury_output;
        long long contestant_output = v.read_integer("value", 0, (long long)1e18);

        // Check that distance are equals
        long long distance_jury = abs(jury_output - pos);
        long long distance_contestant = abs(contestant_output - pos);

        if (distance_jury != distance_contestant) {
            v.WA("The given position is not th best one. got :", contestant_output, " expected :", jury_output, "for value :", pos);
        }
        v.newline();
    }
}