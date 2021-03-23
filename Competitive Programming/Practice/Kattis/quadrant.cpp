#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);

    bool pos_x = (x > 0);
    bool pos_y = (y > 0);

    if (pos_x && pos_y) {
        printf("1");
    } else if (!pos_x && pos_y) {
        printf("2");
    } else if (!pos_x && !pos_y) {
        printf("3");
    } else {
        printf("4");
    }

    return 0;
}