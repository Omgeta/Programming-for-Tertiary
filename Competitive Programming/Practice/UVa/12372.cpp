#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        int x, y, z;
        scanf("%d %d %d", &x, &y, &z);
        printf("Case %d: %s\n", i, (x <= 20 && y <= 20 && z <= 20) ? "good" : "bad");
    }
    return 0;
}