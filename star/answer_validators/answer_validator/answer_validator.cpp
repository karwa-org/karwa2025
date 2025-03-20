#include "validation.h"


int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    AnswerValidator v(argc, argv);

    int answer = v.read_integer("answer", 0, (int)1e9);
    v.newline();
}
