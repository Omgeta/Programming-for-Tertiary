#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {

        int m;
        scanf("%d", &m);

        int low = 0;
        int high = 0;
        int prev;
        scanf("%d", &prev);
        int curr;
        for (int j = 1; j < m; j++) {

            scanf("%d", &curr);
            if (prev < curr) high++;
            else if (prev > curr) low++;
            prev = curr;

        }

        printf("Case %d: %d %d\n", i+1, high, low);
    }

    return 0;
}
