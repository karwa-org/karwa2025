#include "validation.h"

int main(int argc, char *argv[]) {
    std::ifstream in(argv[1]);
    AnswerValidator v(argc, argv);

    int input;
    in >> input;
    int answer = v.read_integer("answer", 1, input);
    v.newline();
}
