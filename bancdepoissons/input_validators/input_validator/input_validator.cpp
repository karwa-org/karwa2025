#include "validation.h"
#include <iostream>
#include <map>

using namespace std;

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int n = v.read_integer("n", 1, 1e5);
    v.newline();
    map<int, bool> unique;
    int maxi = 0;
    for(int i = 0; i < n; i++) {
        int a = v.read_integer("a_i", 0, 1e7);
        if(i != n-1) v.space();
        if(unique[a]) {
            v.WA("The input is not valid not unique positions.");
        }
        unique[a] = true;
        maxi = max(maxi, a);
    }
    v.newline();
    for(int i = 0; i < n; i++) {
        int a = v.read_integer("v_i", 1, 1e7);
        if(i != n-1) v.space();
    }
    v.newline();
    int target = v.read_integer("target_pos", 0, 1e7);
    v.newline();
    if (target < maxi) {
        v.WA("The input is not valid target behind fish.");
    }
    return 0;
}
