#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);

    double sum = 0;
    while (n--) {
        double x, y;
        scanf("%lf %lf", &x, &y);
        sum += x*y;
    }
    printf("%lf\n", sum);


    return 0;
}