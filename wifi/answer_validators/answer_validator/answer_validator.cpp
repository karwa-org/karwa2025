#include "validation.h"
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    AnswerValidator v(argc, argv);

    long long n, q;
    in >> n >> q;

    long long mini = 1e18;
    long long maxi = 0;
    for (int i = 0; i < n; i++) {
        long long val; in >> val;
        mini = min(mini,  val);
        maxi = max(maxi , val);
    }

    for(int i = 0; i < q; i++) {
        v.read_integer("value", mini, maxi);
        v.newline();
    }
}
