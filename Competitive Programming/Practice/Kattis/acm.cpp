#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int x;
    char p;
    char c[5];

    int total = 0, time = 0;
    map<char, int> m;
    while (scanf("%d %c %s", &x, &p, c) == 3) {
        if (c[0] == 'r') {
            total++;
            time += x;
            time += m[p];
        }
        else if (c[0] == 'w') {
            m[p] += 20;
        }
    }
    printf("%d %d\n", total, time);

    return 0;
}