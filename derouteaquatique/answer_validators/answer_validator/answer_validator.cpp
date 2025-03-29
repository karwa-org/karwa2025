#include "validation.h"
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    AnswerValidator v(argc, argv);
    int answer = v.read_integer("answer", 0, 5600);
    v.newline();
}
