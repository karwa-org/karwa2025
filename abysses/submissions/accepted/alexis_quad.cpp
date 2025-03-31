#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

const double EPSILON = 1e-9;

struct karwa_t {
    double x;
    double y;
    int deg;
    int idx;
};

void solve() {
    int n;
    cin >> n;
    vector<karwa_t> karwa(n);

    for (int i = 0; i < n; i++) {
        cin >> karwa[i].x >> karwa[i].y >> karwa[i].deg;
        karwa[i].idx = i;
    }

    int start;
    cin >> start;

    vector<int> next(n, -1);

    for (int i = 0; i < n; ++i) {
        double x0 = karwa[i].x;
        double y0 = karwa[i].y;
        double theta = karwa[i].deg * M_PI / 180.0;
        double dx = cos(theta);
        double dy = sin(theta);

        double min_t = numeric_limits<double>::infinity();
        int best_j = -1;

        for (int j = 0; j < n; ++j) {
            if (i == j) continue;

            double delta_x = karwa[j].x - x0;
            double delta_y = karwa[j].y - y0;

            double t = delta_x * dx + delta_y * dy;
            if (t < -0.0001) continue;

            double distance = abs(delta_x * dy - delta_y * dx);
            if (distance <= 0.0001) {
                if (t < min_t) {
                    min_t = t;
                    best_j = j;
                }
            }
        }

        next[i] = best_j;
    }

    vector<bool> visited(n, false);
    int count = 0;
    int current = start;

    while (current != -1 && !visited[current]) {
        visited[current] = true;
        count++;
        current = next[current];
    }

    cout << count << endl;
}

int main() {
    solve();
    return 0;
}