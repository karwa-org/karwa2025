#include "validation.h"
#include <vector>
#include <iostream>
#include <queue>
// For DYNAMIC OUTPUT PROBLEMS:
// This program will be called as
// output_validator input answer < team_output
//
// Please check the grammar of the team output using the Validator class.
// See input_validator.cpp for information on how to use the Validator class.
// You should also check the validity of the answer here.
// For example, check that a tree printed by the team is a tree indeed.

// For INTERACTIVE PROBLEMS:
// Write your output validator as usual, but make sure to flush all standard
// output. Call `v.set_WA_handler(lambda)` to gracefully handle failures when
// parsing team output. You could e.g. send a '-1' to the submission to tell it
// to stop running.

using namespace std;

const int INF = numeric_limits<int>::max()/2;

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    std::ifstream ans(argv[2]); // Only for custom checker.
    OutputValidator v(argc, argv);

    int n, m, p; in >> n >> m >> p;
    vector<vector<int>> adj(n);
    vector<bool> candidates(n);

    for(int i = 0; i < m; i++){
        int t; in >> t;
        candidates[t] = true;
    }

    for(int i = 0; i < p; i++) {
        int u, v; in >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int n_jury_sol; ans >> n_jury_sol;
    int n_contestant_sol = v.read_integer("ans", 0, 10000);
    v.newline();
    if(n_jury_sol != n_contestant_sol) {
        v.WA("The contestant has not the same number of solutions. got :", n_contestant_sol, " Expected: ", n_jury_sol);
    }

    vector<int> jury_sols;
    for(int i = 0; i < n_jury_sol; i++) {
        int value; ans >> value;
        jury_sols.push_back(value);
    }

    vector<int> contestant_sols;
    for(int i = 0; i < n_contestant_sol; i++){
        int contestant_city = v.read_integer("city", 0, 10000);
        v.space();
        if (candidates[contestant_city] != true) {
            v.WA("The given city is not a candidate city. got :", contestant_city);
        }
        contestant_sols.push_back(contestant_city);
    }
    v.newline();
    sort(jury_sols.begin(), jury_sols.end());
    sort(contestant_sols.begin(), contestant_sols.end());

    for(int i = 0; i < n_jury_sol; i++) {
        if(jury_sols[i] != contestant_sols[i]) {
            v.WA("The given city is not part of the best cities. got :", contestant_sols[i]);
        }
    }
}
