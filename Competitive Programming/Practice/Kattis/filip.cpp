#include <bits/stdc++.h>
using namespace std;

int flip(int n) {
    int reversed = 0;
    while (n > 0) {
        reversed = reversed*10 + n%10;
        n /= 10;
    }
    return reversed;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int x, y;
    scanf("%d %d", &x, &y);
    int a = flip(x);
    int b = flip(y);
    printf("%d\n", max(a, b));

    return 0;
}