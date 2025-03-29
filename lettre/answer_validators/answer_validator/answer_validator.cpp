#include "validation.h"
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    AnswerValidator v(argc, argv);
    std::string answer = v.read_string("answer", 3, 3);
    if (answer != "Oui" && answer != "Non") {
        v.WA("Invalid input: must be 'Oui' or 'Non'");
        return 43;
    }
    v.newline();
    return 0;
}
