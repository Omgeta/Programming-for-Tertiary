#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    scanf("%d", &T);

    while (T--) {
        int N;
        scanf("%d", &N);

        int p = 0;
        int m[100];

        for (int i = 0; i < N; i++) {
            char c[10];
            scanf("%s", c);

            if (c[0] == 'L') p += m[i] = -1;
            else if (c[0] == 'R') p += m[i] = 1;
            else {
                int d;
                scanf("%*s %d", &d);
                p += m[i] = m[d-1];
            }
        }

        printf("%d\n", p);
    }

    return 0;
}