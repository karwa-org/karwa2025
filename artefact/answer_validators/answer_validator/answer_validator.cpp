#include "validation.h"
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    AnswerValidator v(argc, argv);
    int answer = v.read_integer("answer", 0, (long long)2488000000000);
    v.newline();
}
