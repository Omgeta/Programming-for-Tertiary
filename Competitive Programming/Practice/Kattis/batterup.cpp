#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    scanf("%d", &n);

    int total = 0, count = 0;
    while (n--) {
        int x;
        scanf("%d", &x);
        if (x != -1) {
            total += x;
            count++;
        }
    }
    printf("%lf\n", total/(double)count);

    return 0;
}