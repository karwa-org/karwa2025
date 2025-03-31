#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

struct Fish {
    int pos;
    int speed;
};

const int INF = numeric_limits<int>::max() / 2;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, c;
    cin >> n;
    vector<Fish> fishes(n);
    for (int i = 0; i < n; i++) {
        cin >> fishes[i].pos;
    }
    for (int i = 0; i < n; i++) {
        cin >> fishes[i].speed;
    }
    cin >> c;
    
    sort(fishes.begin(), fishes.end(), [](const Fish &a, const Fish &b) {
        return a.pos > b.pos;
    });
    
    int ans = 0;
    double cur_time = 0.0;
    const double EPS = 1e-9;

    for (const auto &f : fishes) {
        double t;
        if (f.speed == 0) {
            t = (f.pos < c) ? INF : 0.0;
        } else {
            t = double(c - f.pos) / f.speed;
        }
        
        if (t - cur_time > EPS) {
            ans++;
            cur_time = t;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
