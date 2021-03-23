#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int v[3];
    scanf("%d %d %d", &v[0], &v[1], &v[2]);
    sort(v, v+3);
    int d1 = v[1] - v[0], d2 = v[2] - v[1];

    if (d1 == d2) {
        printf("%d", v[2] + d1);
    } else if (d1 > d2) {
        printf("%d", v[0] + d2);
    } else {
        printf("%d", v[1] + d1);
    }

    return 0;
}