#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    int diff = abs(a - b);
    char piece[6];
    memcpy(piece, ((diff == 1) ? "piece" : "pieces"), sizeof(piece)); // workaround for ternary operator on c-style string

    if (a < b) {
        printf("Dr. Chaz will have %d %s of chicken left over!\n", diff, piece);
    } else if (a > b) {
        printf("Dr. Chaz needs %d more %s of chicken!\n", diff, piece);
    }

    return 0;
}