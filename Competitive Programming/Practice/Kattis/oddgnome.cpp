#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        int m;
        scanf("%d", &m);

        int prev;
        scanf("%d", &prev);
        for (int j = 0; j < m - 1; j++) {
            int curr;
            scanf("%d", &curr);

            if (prev + 1 != curr) {
                printf("%d\n", j + 2);
                scanf("%*[^\n]s");
                break;
            } else {
                prev = curr;
            }
        }
    }

    return 0;
}