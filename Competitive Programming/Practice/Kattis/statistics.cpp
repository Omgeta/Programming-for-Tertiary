#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    int c = 1;
    while (scanf("%d", &n) == 1) {
        int max = -1e9;
        int min = 1e9;
        int range;
        for (int i = 0; i < n; i++) {
            int curr;
            scanf("%d", &curr);
            
            if (curr > max) max = curr;
            if (curr < min) min = curr;
        }
        range = max - min;
        printf("Case %d: %d %d %d\n", c, min, max, range);
        c++;
    }

    return 0;
}