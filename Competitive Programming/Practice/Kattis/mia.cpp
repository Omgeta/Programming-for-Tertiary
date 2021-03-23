#include <bits/stdc++.h>
using namespace std;

int getScore(int low, int high) {
    if (low > high) {
        swap(low, high);
    }
    if (low == 1 && high == 2) return 1e9;
    if (low == high) return (high * 10 + low) * 10;
    return high * 10 + low;
}

int main() {
    int w, x, y, z;
    while (scanf("%d %d %d %d", &w, &x, &y, &z) == 4 && x != 0) {
        int p1 = getScore(w, x);
        int p2 = getScore(y, z);

        if (p1 > p2) printf("Player 1 wins.\n");
        else if (p1 < p2) printf("Player 2 wins.\n");
        else printf("Tie.\n");
    }

    return 0;
}