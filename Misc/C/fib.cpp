#include <bits/stdc++.h>
using namespace std;

int memo[10001];

int fib_top_down(int n, int memo[]) {
    if (memo[n] != -1) return memo[n];
    int result;
    if (n == 1 || n == 2) result = 1;
    else result = fib_top_down(n-1, memo) + fib_top_down(n-2, memo);
    memo[n] = result;
    return result;
}

int fib_bottom_up(int n) {
    if (n == 1 || n == 2) return 1;
    int bp[10001];
    bp[1] = 1;
    bp[2] = 1;
    for (int i = 3; i <= n; i++)
        bp[i] = bp[i-1] + bp[i-2];
    return bp[n];
}

int fib_iterative(int n) {
    if (n == 1 || n == 2) return 1;
    int x = 1, y = 1, z;
    for (int i = 3; i < n; i++) {
        z = x + y;
        x = y;
        y = z;
    }
    return z;
}

int main() {
    memset(memo, -1, sizeof(memo));

    return 0;
}