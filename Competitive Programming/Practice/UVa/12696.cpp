#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, total = 0;
    scanf("%d", &t);

    while (t--) {
        double x, y, z, k;
        scanf("%lf %lf %lf %lf", &x, &y, &z, &k);
        if (((x <= 56 && y <= 45 && z <= 25) || (x+y+z <= 125)) && k <= 7) {
            printf("1\n"); total++;
        }
        else printf("0\n");
    }
    
    printf("%d\n", total);

    return 0;
}