// TODO
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t, n, k, p;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d %d %d", &n, &k, &p);
        int s = k + p - n;
        printf("Case %d: %d", i, s > 0 ? s : s + n);
    }

    return 0;
}