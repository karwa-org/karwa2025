#include "validation.h"


int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    AnswerValidator v(argc, argv);

    int answer = v.read_integer("answer", 0, (long long)707106780);
    v.newline();
}
