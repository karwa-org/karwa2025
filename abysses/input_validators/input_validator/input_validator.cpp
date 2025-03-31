#include "validation.h"

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int n = v.read_integer("nbr_of_fish", 0, 1000);
    v.newline();

    std::set<std::pair<long long, long long>> fish_positions;
    const long double precision = 1e-5;
    const long double scale = 1e5;

    for (int i = 0; i < n; i++) {
        long double x = v.read_float("pos_x", 0, (long double)1e7);
        v.space();
        long double y = v.read_float("pos_y", 0, (long double)1e7);
        v.space();
        v.read_integer("angle", 0, 359);
        v.newline();

        long long x_scaled = std::llround(x * scale);
        long long y_scaled = std::llround(y * scale);

        if (!fish_positions.insert({x_scaled, y_scaled}).second) {
            v.WA("Two fish are too close to each other.");
        }
    }

    v.read_integer("target_fish", 0, n-1);
    v.newline();
}
