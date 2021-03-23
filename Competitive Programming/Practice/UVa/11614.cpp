// INCOMPLETE
#include <bits/stdc++.h>
using namespace std;
int main() {
    int c;
    scanf("%d", &c);

    for (int i = 0; i < c; i++) {
        long long n;
        scanf("%d", &n);

        for (int j = 1; j <= n; j++) {
            if (n - j <= 0) {
                printf("%d", &j);
                break;
            } 
            n -= j;
        }
    }
    return 0;
}