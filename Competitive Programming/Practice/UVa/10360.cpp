// TLE REDO LATER
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
    int S, d, n, x, y, z, killed[1025][1025];
    memset(killed, 0, sizeof killed);
    scanf("%d", &S);

    while (S--) {
        scanf("%d", &d);
        scanf("%d", &n);
        while (n--) {
            scanf("%d %d %d", &x, &y, &z);
            int i, j;
            for (i = 0; i < 1025; i++) {
                for (j = 0; j < 1025; j++) {
                    if (abs(i - x) <= d && abs(j - x) <= d) {
                        killed[i][j] += z;
                    }
                }
            }
        }

        int m = 0, mX, mY;
        for (int i = 0; i < 1025; i++) {
            for (int j = 0; j < 1025; j++) {
                if (killed[i][j] > m) {
                    m = killed[i][j];
                    mX = i;
                    mY = j;
                }
            }
        }

        printf("%d %d %d\n", mX, mY, m);
    }

    return 0;
}