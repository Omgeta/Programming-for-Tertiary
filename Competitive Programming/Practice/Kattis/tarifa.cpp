#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, n;
    scanf("%d", &x);
    scanf("%d", &n);

    int used = 0;
    for (int i = 0; i < n; i++) {
        int p;
        scanf("%d", &p);
        used += p;
    }

    printf("%d\n", x * (n + 1) - used);

    return 0;
}