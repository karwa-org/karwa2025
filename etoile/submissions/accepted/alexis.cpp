#include <stdio.h>
#include <ostream>
#include <iostream>
#include <math.h>
#include <cassert>

#define int long long
#define double long double

using namespace std;

signed main() {
    int n; cin >> n;
    
    double rho = 4 - 4*2*(1-n);
    if(rho < 0) {
        assert(false);
    }

    double x1 = ((2 + sqrt(rho)) /4);
    cerr << x1 << endl;

    cout << (int)x1 - 1  << endl;
    return 0;
}