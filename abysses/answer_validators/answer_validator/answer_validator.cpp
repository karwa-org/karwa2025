#include "validation.h"
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    AnswerValidator v(argc, argv);

    long long n;
    in >> n;

    v.read_integer("answer", 0, n-1);
    v.newline();
}