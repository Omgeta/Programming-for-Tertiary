#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, y, n;
    scanf("%d %d %d", &x, &y, &n);

    for (int i = 1; i <= n; i++) {
        string o = "";
        if (i % x == 0) o += "Fizz";
        if (i % y == 0) o += "Buzz";
        if (o == "") printf("%d", i);
        else printf("%s", o.c_str());
        printf("\n");
    }

    return 0;
}