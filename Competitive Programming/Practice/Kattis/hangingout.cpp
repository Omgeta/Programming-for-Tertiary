#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int L, N;
    scanf("%d %d", &L, &N);

    int total = 0, denied = 0;
    while (N--) {
        char c[5]; int x;
        scanf("%s %d", c, &x);

        if (c[0] == 'e') {
            if (total + x > L) denied++;
            else total += x;
        }
        else total -= x;
    }
    
    printf("%d", denied);

    return 0;
}