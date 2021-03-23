#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    string last;
    cin >> last;
    bool inc = true;
    bool dec = true;
    for (int i = 1; i < n; ++i) {
        string s;
        cin >> s;
        if (last.compare(s) < 0) {
            dec = false;
        } else if (last.compare(s) > 0) {
            inc = false;
        }
        last = s;
    }
    if (inc) {
        printf("INCREASING\n");
    } else if (dec) {
        printf("DECREASING\n");
    } else {
        printf("NEITHER\n");
    }
    return 0;
}