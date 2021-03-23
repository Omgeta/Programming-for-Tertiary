#include <bits/stdc++.h>
using namespace std;

int main() {
    int l, r;
    scanf("%d %d", &l, &r);
    if ((l == r)) {
        if (l == 0) {
            printf("Not a moose\n");
        }
        else {
            printf("Even %d\n", 2 * l);
        }
    } else {
        printf("Odd %d\n", max(l, r) * 2);
    }

    return 0;
}