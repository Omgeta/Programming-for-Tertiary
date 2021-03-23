#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        int m;
        scanf("%d", &m);

        int max = 0;
        for (int j = 0; j < m; j++) {
            int curr;
            scanf("%d", &curr);
            if (curr > max) max = curr;
        }
        printf("Case %d: %d\n", i+1, max);
    }

    return 0;
}