#include <bits/stdc++.h>
using namespace std;

int g(int n) {
    if (n >= 10) {
        int sum = 0, m;
        while (n > 0) {
            m = n % 10;
            sum += m;
            n /= 10;
        }
        return g(sum);
    } else {
        return n;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int x;
    while (scanf("%d", &x) == 1 && x != 0) {
        int ans = g(x);
        printf("%d\n", ans);
    }

    return 0;
}